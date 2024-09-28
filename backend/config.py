import os
from dotenv import load_dotenv
from sys import platform

basedir = os.path.dirname(__file__)
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    None