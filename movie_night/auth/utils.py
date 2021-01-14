from flask import redirect, url_for
from flask import session, flash
from functools import wraps

def check_login(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "username" not in session:
            flash("Login needed for that")
            return redirect(url_for("auth_bp.login"))
        return func(*args, **kwargs)
    return wrapped_func