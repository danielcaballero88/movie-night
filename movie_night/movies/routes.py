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
# Utilities
from movie_night.auth.utils import login_needed, logout_needed
from .utils.imdb_api import ia

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
        # Check if a title is already given
        mvttl = request.args.get("title")
        movies = ia.search_movie(mvttl) if mvttl else None
        return render_template("add_movie.html", movies=movies)
    # POST
    # Get movies imdb ids from the form
    chkmvs = request.form.getlist("checkmovies")
    # Create and add the objects to the database
    for chkmv in chkmvs:
        ttl, yr, imid, cvurl = chkmv.split(';')
        movie = Movie(title=ttl, year=yr, imdb_id=imid, cover_url=cvurl, user_id=int(current_user.get_id()))
        db.session.add(movie)
    db.session.commit()
    flash(f"Movies added: {chkmvs}")
    return redirect(url_for('.user'))

@movies_bp.route("/del_movie/", methods=["POST"])
@login_needed
def del_movie():
    mvttl = request.form["title"]
    movie = Movie.query.filter_by(title=mvttl)
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
        usr = User.query.filter_by(id=usr_id).first()
        users.append(usr)
    movies = zip(movies,users)
    return render_template("list_all.html", movies=movies)
