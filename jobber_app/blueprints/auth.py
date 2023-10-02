from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    Response,
    url_for
)
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
            new_user = User(username=username, email=email)
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
        pass

    return render_template("login.html")