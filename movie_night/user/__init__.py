from flask import Blueprint

# Blueprint Configuration
user_bp = Blueprint(
    "user_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

from . import routes