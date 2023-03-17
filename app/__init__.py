"""when you import 'app' as package  __init__.py performs and determiens 
which characters provide the package """

from flask import Flask
# import configuration Class
from config import Config
#database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#login
from flask_login import LoginManager

#create an application object
app = Flask(__name__)
app.config.from_object(Config) # use configuration from class Config
db = SQLAlchemy(app) # database object
migrate = Migrate(app,db) # migration object
login = LoginManager(app) # login
login.login_view = 'login' # function to login

#import URLs , route handlers, models(databases structure)
from app import routes, models