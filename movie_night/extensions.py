"""
I create here global instance of each extension (instead of in root init.py)
to avoid circular imports that could occur if in the future they are imported
from the root init.py (which in turn imports all other things?)
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_login import LoginManager

# Define a naming convention to avoid unnamed constraints in sqlite
# because that could lead to errors when applying migrations
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# Apply the naming convention to a metadata object
metadata = MetaData(naming_convention=convention)

# Create global instances
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
login_manager = LoginManager()
