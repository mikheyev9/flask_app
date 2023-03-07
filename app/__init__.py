"""when you import 'app' as package  __init__.py performs and determiens 
which characters provide the package """

from flask import Flask
# import configuration Class
from config import Config
#database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create an application object
app = Flask(__name__)
app.config.from_object(Config) # use configuration from class Config
db = SQLAlchemy(app) # database object
migrate = Migrate(app,db) # migration object

#import URLs , route handlers, models(databases structure)
from app import routes, models