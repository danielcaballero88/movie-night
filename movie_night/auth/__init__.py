from flask import Blueprint

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

from . import routes