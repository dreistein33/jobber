from flask import Blueprint, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .validation import is_user_in_db
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        if is_user_in_db(email=email, name=username):
            # To change later to display nicely
            return "User already exists!"

        

    # Return register form as default as if there are any other 
    # request method than POST
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Change session state that will indicate if user is log on"""

    if request.method == "POST":
        pass

    return render_template("login.html")