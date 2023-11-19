from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    Response,
    url_for
)
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..database.models import User
from ..validation import is_user_in_db
from .. import db


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        print(email, username, password)

        # Create new User object

        try:
        # Add user to database
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.create_password_hash(password)
            db.session.add(new_user)
            db.session.commit()
            print("success")

            # Return succes page defined in main blueprint
            return redirect(url_for("home.register_success"))

        # Return 
        except AssertionError as error_message:
            return Response(
                str(error_message),
                status=400
            )

    # Return register form as default as if there are any other 
    # request method than POST
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Change session state that will indicate if user is log on"""

    if request.method == "POST":
        username = request.form.get("username") 
        password = request.form.get("password")

        try:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                redirect(url_for("auth.profile"))

            else:
                return f"bad username or password!"


        except AssertionError as error_message:
            return f"{error_message}"

    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()


@auth.route("/profile")
@login_required
def profile():
    return f"Witaj {current_user.username}"


