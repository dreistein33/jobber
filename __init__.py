from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    from .config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig()) 

    CORS(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .rest_api import rest_api as rest_api_blueprint
    app.register_blueprint(rest_api_blueprint)

    return app

