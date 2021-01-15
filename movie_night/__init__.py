"""Initialize Flask app."""
from flask import Flask
from config import config

def create_app(config_name):
    """Create Flask application."""
    # Create app
    app = Flask(__name__, instance_relative_config=False)
    # Import configuration from config file
    app.config.from_object(config[config_name])
    # Initialize database
    from .database import db
    db.init_app(app)
    #
    with app.app_context():
        # Register Blueprints
        from .home import home_bp
        from .auth import auth_bp
        from .movies import movies_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(movies_bp, url_prefix="/movies/")
        # Create tables (only the first time?)
        db.create_all()
        # Done
        return app