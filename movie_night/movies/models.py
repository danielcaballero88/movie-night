""" Models for user blueprint
each model is something that a user can store or save """

from movie_night.database import db

class Movie(db.Model):
    """ List of movies
    Each user can store many movies
    Each movie belongs (for now) only to one user
    Relation: one to many (one user to many movies) """
    # Table name
    __tablename__ = 'movies'
    # Id: primary key
    _id = db.Column(
        'id',
        db.Integer,
        primary_key=True
    )
    # Name field
    name = db.Column(
        db.String,
        unique=True,
        nullable=False
    )
    # User (parent) field: foreign key
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return self.name

    def get_id(self):
        return self._id
