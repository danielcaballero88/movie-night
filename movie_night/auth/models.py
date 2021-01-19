"""Models for user Blueprint"""
from movie_night.extensions import db
from movie_night.extensions import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """ Data model for user accounts """
    # Table: name
    __tablename__ = "user"
    # Field: Primary key
    id = db.Column(
        "id",
        db.Integer,
        primary_key=True
    )
    # Field: username
    username = db.Column(
        db.String(60),
        unique=True,
        nullable=False
    )
    # Field: email
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    # Field: password_hash
    password_hash = db.Column(
        db.String(128),
        nullable=False
    )
    # Relationship: User pelis
    movies = db.relationship("Movie")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, pswrd):
        self.password_hash = generate_password_hash(pswrd)

    def check_password(self, pswrd):
        return check_password_hash(self.password_hash, pswrd)

@login_manager.user_loader
def load_user(_id):
    return User.query.get(int(_id))
