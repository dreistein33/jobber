from dataclasses import dataclass
from flask_login import UserMixin
import re
from sqlalchemy import func, event
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dataclass
class ErrorMessage:
    """Boilerplate Class for Error messages."""

    # NOTE TO SELF
    # MIGHT WANT TO MOVE THAT TO ANOTHER FILE LATER

    NO_PASSWORD: str = "No password provided."
    BAD_PASSWORD_LEN: str = "Password must be minimum 5 and maximum 50 characters long."
    BAD_PASSWORD_CHAR: str = "Password must contain at least 1 great letter, digit and special character."

    NO_USERNAME: str = "No username provided."
    BAD_USERNAME_LENGTH: str = "Username must be between 3 and 32 characters long."
    
    USER_EXISTS: str = "User already exists."

    NO_EMAIL: str = "No email provided."
    BAD_EMAIL_PATTERN: str = "Provided email is not valid email address."


class User(UserMixin, db.Model):
    
    # Global user info
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # Preset form info

    # Manage passwords: generate, check
    def create_password_hash(self, password: str) -> None:
        if not password:
            raise AssertionError(ErrorMessage.NO_PASSWORD)
        
        if len(password) not in range(5, 51):
            raise AssertionError(ErrorMessage.BAD_PASSWORD_LEN)

        # Check if password contains at least one great letter, one small letter, digit, and special char
        password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])"
        if not re.match(password_pattern, password):
            raise AssertionError(ErrorMessage.BAD_PASSWORD_CHAR)
        
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if not password:
            raise AssertionError(ErrorMessage.NO_PASSWORD)

        return check_password_hash(self.password_hash, password)

    # Validate input data

    @validates("username")
    def validate_username(self, username):
        return username

    @validates("email")
    def validate_email(self, email):      
        return email


@event.listens_for(User, 'before_insert')
def validate_email_before_insert(mapper, connection, target):
    # Tutaj możesz wywołać funkcję validate_email przed wstawieniem nowego rekordu do bazy danych
    if not target.email:
        raise AssertionError(ErrorMessage.NO_EMAIL)

    if User.query.filter_by(email=target.email).first():
        raise AssertionError(ErrorMessage.USER_EXISTS)

    email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_pattern, target.email):
        raise AssertionError(ErrorMessage.BAD_EMAIL_PATTERN)


@event.listens_for(User, "before_insert")
def validate_username_before_insert(mapper, connection, target):
        if not username:
            raise AssertionError(ErrorMessage.NO_USERNAME)
        
        if User.query.filter_by(username=username).first():
            raise AssertionError(ErrorMessage.USER_EXISTS)

        if len(username) not in range(3, 33):
            raise AssertionError(ErrorMessage.BAD_USERNAME_LENGTH)