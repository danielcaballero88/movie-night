"""General page routes."""
from . import home_bp
from flask import current_app as app
from flask import render_template

@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    return render_template("index.html")

@home_bp.route("/about/", methods=["GET"])
def about():
    """About page."""
    return render_template("about.html")

@home_bp.route("/contact/", methods=["GET"])
def contact():
    """Contact page."""
    return render_template("contact.html")