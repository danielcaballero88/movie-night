""" Authentication pages """
# Flask
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import request, session, flash
# Login
from flask_login import current_user, login_user, logout_user
# Database
from movie_night.extensions import db
# Models
from .models import User
# Forms
from .forms import LoginForm, RegisterForm
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

@auth_bp.route("/register/", methods=["GET", "POST"])
@logout_needed
def register():
    """ Create an account """
    frm = RegisterForm()
    if request.method == "GET":
        return render_template("register.html", form=frm)
    # POST
    if frm.validate():
        # Get form data
        usrnm = frm.username.data
        emads = frm.email.data
        pswrd = frm.password.data
        # Create new user
        usr = User(username=usrnm, email=emads, password=pswrd)
        db.session.add(usr)
        db.session.commit()
        flash("Registration Successful")
        return redirect(url_for(".login"))
    # Form invalid
    flash("Form invalid")
    return render_template("register.html", form=frm)

@auth_bp.route("/login/", methods=["GET", "POST"])
@logout_needed
def login():
    """ Login to a user account """
    frm = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=frm)
    #
    # POST
    if frm.validate():
        # Get form data
        usrnm = frm.username.data
        pswrd = frm.password.data
        rmmbr = frm.remember.data
        # Authenticate User
        usr = User.query.filter_by(username=usrnm).first()
        if not usr or not usr.check_password(pswrd):
            flash("Not a user or wrong password")
            return redirect(url_for(".login"))
        # else: Success
        login_user(usr, remember=rmmbr)
        # Done
        flash(f"Login Success for user {usrnm}, remember={rmmbr}")
        return redirect(url_for("home_bp.home"))
    # INVALID FORM
    flash("Invalid form")
    return render_template('login.html', form=frm)

@auth_bp.route("/logout/", methods=["GET", "POST"])
@login_needed
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logout success")
    return redirect(url_for("home_bp.home"))