from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    from .config import DevelopmentConfig
    # Bind the config to app
    app.config.from_object(DevelopmentConfig()) 

    # Allow making requests to the same endpoint
    CORS(app)

    # Use config for database from Flask app configuration
    db.init_app(app)

    # Import blueprints for Flask app
    from blueprints import (
        auth_blueprint,
        main_blueprint,
        rest_api_blueprint
    )

    # Register blueprints so it will allow usage of its namespace
    app.register_blueprint(auth_blueprint)              # "auth"
    app.register_blueprint(main_blueprint)              # "main"
    app.register_blueprint(rest_api_blueprint)          # "rest_api"

    return app

