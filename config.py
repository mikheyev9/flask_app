# configuration class

import os  # operating system module

basedir = os.path.abspath(os.path.dirname(__file__)) #path to this folder

class Config(object):
    #environment variable value is preferred
    SECRET_KEY = os.environ.get('SECRET_KEY') or "You-will-never-guess"
    #environment of database from configuration variable or basedir/app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                'sqlite:///'+os.path.join(basedir,'app.db')