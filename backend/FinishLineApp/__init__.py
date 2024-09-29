from flask import Flask
from .extensions import db, migrate
from datetime import datetime


def create_app(config_name='DevConfig'):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

    app.config.from_prefixed_env()
    app.config.from_object('config.%s' % config_name)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Event, EventTag, db_fill_samples, db_verify_sample_data

    with app.app_context():
        db.create_all()

        db_fill_samples()
        db_verify_sample_data()
    
    from .blueprints import api_bp

    app.register_blueprint(api_bp)

    return app