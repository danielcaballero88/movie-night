"""Models for user Blueprint"""
from movie_night.database import db

class User(db.Model):
    """ Data model for user accounts """
    # Table: name
    __tablename__ = "user"
    # Field: Primary key
    _id = db.Column(
        "id",
        db.Integer,
        primary_key=True
    )
    # Field: name
    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    # Field: password
    password = db.Column(
        db.String(100),
        nullable=False
    )
    # Relationship: User pelis
    movies = db.relationship("Movie")

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return self.name

    def get_id(self):
        return self._id
