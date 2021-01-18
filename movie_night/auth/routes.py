""" Authentication pages """
# Flask
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import request, session, flash
# Database
from movie_night.database import db
# Models
from .models import User
# Forms
from .forms import LoginForm
# Utils
from .utils import login_needed, logout_needed
# Blueprint (self)
from flask import Blueprint


# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@auth_bp.route("/signup/", methods=["GET", "POST"])
@logout_needed
def signup():
    """ Create an account """
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        # get form data
        username = request.form["username"]
        userpass = request.form["userpass"]
        new_usr = User(username, userpass)
        db.session.add(new_usr)
        db.session.commit()
        flash("Sign Up Success")
        return redirect(url_for("auth_bp.login"))

@auth_bp.route("/login/", methods=["GET", "POST"])
@logout_needed
def login():
    """ Login to a user account """
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    #
    # POST
    if form.validate():
        # Prepare session
        session.permanent = True
        # Get form data
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        # Authenticate User
        found_user = User.query.filter_by(name=username).first()
        if not found_user:
            flash("Not a user")
            return redirect(url_for("auth_bp.login"))
        if password != found_user.password:
            flash("Wrong password")
            return redirect(url_for("auth_bp.login"))
        # else: Success
        session["username"] = username
        # Done
        flash(f"Login Success for user {username}, remember={remember}")
        return redirect(url_for("home_bp.home"))
    # INVALID FORM
    flash("Invalid form")
    return render_template('login.html', title='Sign In', form=form)

@auth_bp.route("/logout/", methods=["GET", "POST"])
def logout():
    if "username" in session:
        username = session["username"]
        flash(f"Logout successful, bye {username}!", "info")
        session.pop("username", None)
    else:
        flash("No one to loggout ¬¬")
    return redirect(url_for("home_bp.home"))