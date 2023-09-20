# Display Frontend

from flask import Blueprint, render_template
from flask_cors import CORS

main = Blueprint("main", __name__)


@main.route("/")
def home():
    # NOTE TO SELF
    # This should display different versions regarding session state described in auth.py

    return render_template("form.html")
