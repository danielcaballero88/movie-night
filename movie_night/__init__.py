"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Global database variable
db = SQLAlchemy()

def create_app():
    """Create Flask application."""
    # Create app
    app = Flask(__name__, instance_relative_config=False)
    # Import configuration from config file
    app.config.from_object("config.DevConfig")
    # Initialize database
    db.init_app(app)
    #
    with app.app_context():
        # Register Blueprints
        from .home import home_bp
        from .auth import auth_bp
        from .user import user_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp, url_prefix="/user/")
        # Create tables (only the first time?)
        db.create_all()
        # Done
        return app