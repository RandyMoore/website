# Auth - override these to real values with prod_config.py
ADMIN_USER = "admin" # Username to create / edit blogs
# Password is "secret"
SALT = "salt"
HASH = "$6$rounds=656000$ux9h9j92H1T3ZiS9$aWPRho0WpU9eyVCmuVt36yhBXBAVapiiWEmTqAJBErwCsEY9VefoFR//f6JrO4ktZmobM8.C55BxjMSCklV6x0"

# Flask-blogging configs
BLOGGING_URL_PREFIX = "/blog"
BLOGGING_SITENAME = "Blog of Randy Moore"
FILEUPLOAD_IMG_FOLDER = "fileupload"
FILEUPLOAD_PREFIX = "/fileupload"
FILEUPLOAD_ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
BLOG_DB = "sqlite:///blog.db"

