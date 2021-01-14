""" db variable set in its own module to avoid
circular imports (which would happen if I later import db from
the root __init__.py, which in turns import all things?) """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
