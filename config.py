from msilib.schema import Environment
import os

# set the app secret key
SECRET_KEY = os.urandom(32)
# get the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# connection information
username = 'postgres'
password = '21101682'
DATABASE_NAME = 'plants'

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@localhost:5432/{}'.format(username, password, DATABASE_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
ENVIRONMENT = 'development'