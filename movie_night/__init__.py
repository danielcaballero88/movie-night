"""Initialize Flask app."""
# Flask
from flask import Flask
# Configuration
from config import config
# Extensions
from .extensions import db # flask_sqlalchemy
from .extensions import migrate #  flask_migrate
from .extensions import login_manager # flask_login

def create_app(config_name):
    """Create Flask application."""
    # Create app
    app = Flask(__name__, instance_relative_config=False)
    # Import configuration from config file
    app.config.from_object(config[config_name])
    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    # Initialize login manager
    login_manager.init_app(app)
    # Register Blueprints
    with app.app_context():
        # Register Blueprints
        from .home import home_bp
        from .auth import auth_bp
        from .movies import movies_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(movies_bp, url_prefix="/movies/")
        # Create/init database
        if False:
            # Commented out because it is a one time thing
            # achieved better from cli by: flask db init
            # (needed flask_migrate for this)
            # Create tables (only the first time?)
            db.create_all()
        # Done
        return app