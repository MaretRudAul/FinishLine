from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_prefixed_env()
    app.config.from_object('config.py')

    db.init_app(app)

    return app