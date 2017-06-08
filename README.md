# Website (what a creative name!)
Everything needed to deploy my personal website (content persisted in DB not included).  Flask based app wrapped in Dockerized Nginx.

## Setup
**Flask Debug Mode**  
Create a python virtual environment at the project root:  
`virtualenv .`  
This will allow installation of the app's dependencies in the project directory they do not mess with your global Python environment.  Next enter the virtual environment.
`source bin/activate`

Install the application  
`cd app`  
`pip install --editable .`  
The "editable" is so that when you deploy the app in debug mode it automatically reloads when you make code or resource changes - very fast development iteration.  To run in debug mode and have the site accessible at localhost:5000  
`./run_debug.sh`

You can click on the Blog link and then login using "admin" and "secret" as the default username and password to create blog posts and play around.  

To exit the python virtual environment type  
`deactivate`

Running the app in debug mode should always be done first to create the blog database app/blog.db  For a currently unknown reason running the app using nginx will result in a SQLAlchemy error complaining it can't find blog.db, but if it already exists all is well.

**Nginx**  
First create blog.db - run the app in Flask Debug Mode as above.  You will also need to have Docker installed on your machine.  From the project root  
`docker-compose up`  
A single Docker container will be created with Nginx using uWSGI to communicate with the application via a socket.

## WIP Disclaimer
Yes this is a work in progress.  There's some code duplication, things need to be cleaned up, etc.  At this point using docker-compose is overkill since there's only one container - but that will probably change in the future :)