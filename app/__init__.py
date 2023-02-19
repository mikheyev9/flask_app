"""when you import 'app' as package  __init__.py performs and determiens 
which characters provide the package """

from flask import Flask
# import configuration Class
from config import Config

#create an application object
app = Flask(__name__)
app.config.from_object(Config) # use configuration from class Config

#import URLs , route handlers
from app import routes