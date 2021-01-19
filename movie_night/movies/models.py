""" Models for user blueprint
each model is something that a user can store or save """

from movie_night.extensions import db

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
    # Field: title
    title = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    # Field: year
    year = db.Column(
        db.Integer,
        unique=False,
        nullable=True
    )
    # Field: IMDb id
    imdb_id = db.Column(
        db.Integer,
        unique=True,
        nullable=True
    )
    # Field: cover_url
    cover_url = db.Column(
        db.String(240),
        unique=False,
        nullable=True
    )
    # User (parent) field: foreign key
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    def __init__(self, title, year, imdb_id, cover_url, user_id):
        self.title = title
        self.year = year
        self.imdb_id = imdb_id
        self.cover_url = cover_url
        self.user_id = user_id

    def __str__(self):
        return self.name

    def get_id(self):
        return self._id
