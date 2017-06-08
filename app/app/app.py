from flask import Flask, render_template, redirect, request
from sqlalchemy import create_engine, MetaData
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_blogging import SQLAStorage, BloggingEngine
from passlib.apps import custom_app_context as pwd_context
from passlib import pwd


app = Flask(__name__)

app.config.from_object('app.default_config')
try:
    app.config.from_object('app.prod_config')  # Override default values w/ secret values
except ImportError:
    pass

app.secret_key = pwd.genword()
engine = create_engine(app.config["BLOG_DB"])
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
login_manager = LoginManager(app)
meta.create_all(bind=engine)

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')


@app.route("/login/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if pwd_context.verify(app.config['SALT'] + request.form['username'] + request.form['password'], app.config['HASH']):
            user = User(app.config['ADMIN_USER'])
            login_user(user)
            return redirect("/blog")
        else:
            error = 'Invalid username / password'
    return render_template('login.html', error=error)


@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")


# For Blog
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)