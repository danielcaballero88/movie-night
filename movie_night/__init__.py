"""Initialize Flask app."""
from flask import Flask

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    with app.app_context():
        # Register Blueprints
        from .home import home_bp
        from .auth import auth_bp
        from .user import user_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp, url_prefix="/user/")

        return app