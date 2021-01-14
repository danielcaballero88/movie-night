""" Flask configuration """

import os
from dotenv import load_dotenv

here_path = os.path.dirname(__file__)
dotenv_path = os.path.join(here_path, '.env')
load_dotenv(dotenv_path=dotenv_path)

class Config:
    """ Base Config """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """ Development Config """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class ProdConfig(Config):
    """ Production Config """
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
