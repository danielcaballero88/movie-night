"""Models for user Blueprint"""
from movie_night import db

class Users(db.Model):
    """ Data model for user accounts """
    # Table: name
    __tablename__ = "users"
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
    # # Relationship: User pelis
    # pelis = db.relationship(
    #     "PeliList",
    #     back_populates="users"
    # )