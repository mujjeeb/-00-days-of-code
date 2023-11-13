from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

MOVIE_DB_API_KEY = "9f80230492f163037e6bae90e9ea7f2c"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie/"



##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top10-movies.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(300), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(300), unique=True, nullable=True)
    img_url = db.Column(db.String(300), unique=True, nullable=False)


app.app_context().push()
db.create_all()


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/delete<int:index>", methods=['GET', 'POST'])
def delete(index):
    all_movies = db.session.query(Movie).all()
    for movie in all_movies:
        if movie.id == index:
            movie_to_delete = Movie.query.get(movie.id)
            db.session.delete(movie_to_delete)
            db.session.commit()
    return redirect(url_for("home"))


# Create form for adding a new movie
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


# Create form for editing rating and reviews of movies
class ChangeForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g 8.5', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])
    submit = SubmitField('Done')


@app.route("/edit<int:index>", methods=['GET', 'POST'])
def edit(index):
    all_movies = db.session.query(Movie).all()
    form = ChangeForm()
    for movie in all_movies:
        if movie.id == index:
            requested_movie = movie
            if form.validate_on_submit():
                new_rating = form.rating.data
                new_review = form.review.data
                movie_to_update = Movie.query.get(requested_movie.id)
                movie_to_update.rating = new_rating
                movie_to_update.review = new_review
                db.session.commit()
    return render_template('edit.html', movie=requested_movie, form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        movie_db_image_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}/images"
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{movie_db_image_url}{data['poster_path']}",
            description=data["overview"],
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))




if __name__ == '__main__':
    app.run(debug=True)
