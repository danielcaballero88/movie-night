from flask import redirect, url_for
from flask import session, flash
from functools import wraps

def login_needed(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "username" not in session:
            print("login_needed")
            flash("Login needed for that")
            return redirect(url_for("home_bp.home"))
        return func(*args, **kwargs)
    return wrapped_func

def logout_needed(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "username" in session:
            usrnm = session["username"]
            flash(f"Already logged in as {usrnm}")
            return redirect(url_for("home_bp.home"))
        return func(*args, **kwargs)
    return wrapped_func