""" User pages """
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import session, flash, request
from . import user_bp

@user_bp.route("/", methods=["GET", "POST"])
def user():
    if not "username" in session:
        flash("Not logged in")
        return redirect(url_for("home_bp.home"))
    if request.method == "GET":
        usr_nm = session["username"]
        return render_template("user.html", username=usr_nm)
    # POST
    return redirect(url_for("home_bp.home"))