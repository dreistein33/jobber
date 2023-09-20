from flask_login import UserMixin
from sqlalchemy import func
from . import db


class User(UserMixin, db.Model):
    
    # Global user info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Preset form info
    