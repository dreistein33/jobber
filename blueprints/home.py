# Display Frontend

from flask import Blueprint, render_template
from flask_cors import CORS

home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    # NOTE TO SELF
    # This should display different versions regarding session state described in auth.py

    return render_template("form.html")


@home.route("/success/")
def register_success():
    # Show page that confirms correct signup with given username

    return render_template("success.html")
