from flask import Flask
from .extensions import db, migrate, cors
from datetime import datetime
from .commands import register_commands


def create_app(config_name='DevConfig'):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')

    app.config.from_prefixed_env()
    app.config.from_object('config.%s' % config_name)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    register_commands(app)

    with app.app_context():
        db.create_all()
    
    from .blueprints import api_bp

    app.register_blueprint(api_bp)

    return app