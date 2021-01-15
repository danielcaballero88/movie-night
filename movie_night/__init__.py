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
    from .database import db, migrate
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    #
    with app.app_context():
        # Register Blueprints
        from .home import home_bp
        from .auth import auth_bp
        from .movies import movies_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(movies_bp, url_prefix="/movies/")
        if False:
            # Commented out because it is a one time thing
            # achieved better from cli by: flask db init
            # (needed flask_migrate for this)
            # Create tables (only the first time?)
            db.create_all()
        # Done
        return app