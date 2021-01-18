from flask import redirect, url_for
from flask import flash
from functools import wraps
from flask_login import current_user

def login_needed(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if current_user.is_anonymous:
            print("login_needed")
            flash("Login needed for that")
            return redirect(url_for("home_bp.home"))
        return func(*args, **kwargs)
    return wrapped_func

def logout_needed(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if current_user.is_authenticated:
            usrnm = current_user.username
            flash(f"Already logged in as {usrnm}")
            return redirect(url_for("home_bp.home"))
        return func(*args, **kwargs)
    return wrapped_func