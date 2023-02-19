# configuration class

import os  # operating system module

class Config(object):
    #environment variable value is preferred
    SECRET_KEY = os.environ.get('SECRET_KEY') or "You-will-never-guess"