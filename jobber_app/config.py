# App Configuration 
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
print(BASE_DIR)


class Config:
    """Parent config class that child classes will inherit from
       for testing, production and development."""

    # THIS DOESNT WORK FFS :--DDDD fixfixifix
    load_dotenv(path.join(BASE_DIR, ".env"))
    
    # General
    SECRET_KEY = environ.get("FLASK_SECRET_KEY")
    STATIC_FOLDER = path.join(BASE_DIR, "static") 
    TEMPLATES_FOLDER = path.join(BASE_DIR, "templates") 

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:////home/dzony/jobber/jobber_app/database/db.sqlite"


class DevelopmentConfig(Config):
    pass