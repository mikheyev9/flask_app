# configuration class

import os  # operating system module

basedir = os.path.abspath(os.path.dirname(__file__)) #path to this folder

class Config(object):
    #environment variable value is preferred
    SECRET_KEY = os.environ.get('SECRET_KEY') or "You-will-never-guess"
    #environment of database from configuration variable or basedir/app.db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db') #os.environ.get('DATABASE_URL')
    #for emails
    MAIL_SERVER= 'localhost' #os.environ.get('MAIL_SERVER')
    MAIL_PORT = 8025 #int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@exaple.com']
    POSTS_PER_PAGE = 3