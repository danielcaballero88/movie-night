""" Authentication pages """
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import request, session, flash
from .models import Users
from . import auth_bp

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
    found_user = Users.query.filter_by(name=username).first()
    if not found_user:
        flash("Not a user")
        return redirect(url_for("auth_bp.login"))
    if userpass != found_user.password:
        flash("Wrong password")
        return redirect(url_for("auth_bp.login"))
    # else: Success
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