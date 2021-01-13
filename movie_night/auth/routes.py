""" Authentication pages """
from . import auth_bp
from flask import current_app as app
from flask import redirect, url_for
from flask import render_template
from flask import request
from flask import session
from flask import flash

@auth_bp.route("/login/", methods=["GET", "POST"])
def login():
    if "username" in session:
        flash(f"Already logged as {session['username']}")
        return redirect(url_for("home_bp.home"))
    if request.method == "GET":
        return render_template("login.html")
    # POST
    # Prepare session
    session.permanent = True
    # Get form data
    username = request.form["username"]
    userpass = request.form["userpass"]
    # Authenticate User
    session["username"] = username
    # Done
    flash("Login Success")
    return redirect(url_for("home_bp.home"))

@auth_bp.route("/logout/", methods=["GET", "POST"])
def logout():
    if "username" in session:
        username = session["username"]
        flash(f"Logout successful, bye {username}!", "info")
        session.pop("username", None)
    else:
        flash("No one to loggout ¬¬")
    return redirect(url_for("home_bp.home"))