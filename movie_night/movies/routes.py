""" User pages """
# Flask imports
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import session, flash, request
# Extensions
from movie_night.extensions import db
from flask_login import current_user
# Models
from movie_night.auth.models import User
from .models import Movie
# Blueprint (self) import
from flask import Blueprint

from movie_night import auth
from movie_night.auth.utils import login_needed, logout_needed

# Blueprint Configuration
movies_bp = Blueprint(
    "movies_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@movies_bp.route("/user/", methods=["GET"])
@login_needed
def user():
    """ User personal page """
    usr = current_user
    return render_template("user.html", user=usr)

@movies_bp.route("/add_movie/", methods=["GET", "POST"])
@login_needed
def add_movie():
    """ Add movie form """
    if request.method == "GET":
        return render_template("add_movie.html")
    # POST
    mov_nm = request.form["moviename"]
    usr = current_user
    usr_id = usr._id
    new_movie = Movie(name=mov_nm, user_id=usr_id)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('.user'))

@movies_bp.route("/del_movie/", methods=["POST"])
@login_needed
def del_movie():
    movie_name = request.form["movie2del"]
    movie = Movie.query.filter_by(username=movie_name)
    print(movie, type(movie))
    print(movie.first(), type(movie.first()))
    movie.delete()
    db.session.commit()
    return redirect(url_for('.user'))

@movies_bp.route("/list_all/", methods=["GET"])
@login_needed
def list_all():
    movies = Movie.query.all()
    users = []
    for movie in movies:
        usr_id = movie.user_id
        usr = User.query.filter_by(_id=usr_id).first()
        users.append(usr)
    movies = zip(movies,users)
    return render_template("list_all.html", movies=movies)
