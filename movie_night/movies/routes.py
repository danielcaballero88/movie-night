""" User pages """
# Flask imports
from flask import current_app as app
from flask import redirect, url_for, render_template
from flask import session, flash, request
# Database and Models imports
from movie_night.database import db
from movie_night.auth.models import User
from .models import Movie
# Blueprint (self) import
from flask import Blueprint

# Blueprint Configuration
movies_bp = Blueprint(
    "movies_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@movies_bp.route("/user/", methods=["GET"])
def user():
    """ User personal page """
    if "username" not in session:
        flash("Not logged in")
        return redirect(url_for("home_bp.home"))
    usr_nm = session["username"]
    usr = User.query.filter_by(name=usr_nm).first()
    return render_template("user.html", user=usr)

@movies_bp.route("/add_movie/", methods=["GET", "POST"])
def add_movie():
    """ Add movie form """
    if request.method == "GET":
        return render_template("add_movie.html")
    # POST
    mov_nm = request.form["moviename"]
    usr_nm = session["username"]
    usr = User.query.filter_by(name=usr_nm).first()
    usr_id = usr.get_id()
    new_movie = Movie(name=mov_nm, user_id=usr_id)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('.user'))

@movies_bp.route("/del_movie/", methods=["POST"])
def del_movie():
    movie_name = request.form["movie2del"]
    movie = Movie.query.filter_by(name=movie_name)
    print(movie, type(movie))
    print(movie.first(), type(movie.first()))
    movie.delete()
    db.session.commit()
    return redirect(url_for('.user'))