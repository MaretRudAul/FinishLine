from flask import Flask
from .extensions import db, migrate


def create_app(config_name='DevConfig'):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

    app.config.from_prefixed_env()
    app.config.from_object('config.%s' % config_name)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Event, EventTag

    with app.app_context():
        db.create_all()

    return app