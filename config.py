# App Configuration 
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Parent config class that child classes will inherit from
       for testing, production and development."""
    
    # General
    SECRET_KEY = environ.get("FLASK_SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")


class DevelopmentConfig(Config):
    pass