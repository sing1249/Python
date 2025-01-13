from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



# CREATE DB
class Base(DeclarativeBase):
  pass
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

#Creating the extension.
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

#Defining the model for db
class Movie(db.Model): #Creating the Movie class with db.Model as inheritance.
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable= False, unique=True)
    year: Mapped[str] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[str] = mapped_column(Float, nullable=True)
    ranking: Mapped[str] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250))

# CREATE TABLE
with app.app_context():
    db.create_all()

#Adding a movie to the database.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )


# with app.app_context():
#     db.session.add(second_movie)
#     db.session.add(new_movie)
#     db.session.commit()




@app.route("/")
def home():
    #To display the movies, I will have to read the data from the database using scalars
    with app.app_context():
        all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
        #Used to all() to fetch all the movies into a list.

    #Sorting the movies on the home page.
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

#Creating the WTForm for changing the movie rating
class UpdateRating(FlaskForm):
    updated_rating = StringField('Your rating out of 10', validators=[DataRequired()])
    updated_review = StringField('Your review', validators=[DataRequired()])
    done = SubmitField(label="Update")

@app.route("/update", methods=['GET', 'POST'])
def update():
    update_form = UpdateRating()
    movie_id = request.args.get('id')  # Will get the id from the URL that gets dynamically generated when user click on Update link.
    if update_form.validate_on_submit():
        new_rating = update_form.updated_rating.data
        new_review = update_form.updated_review.data
        with app.app_context():
            ratings_update = db.get_or_404(Movie, movie_id) #Getting hold of movie using id from arg to update
            ratings_update.rating = new_rating
            ratings_update.review = new_review
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=update_form)


#To delete a movie, movie_id will be gathered from the URL using request.args.get and then it will be used to get
#hold of the movie in the db and then delete it.
@app.route("/delete", methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    movie_to_be_deleted = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_be_deleted)
    db.session.commit()
    return redirect(url_for('home'))

#Adding a new movie to the database
#Creating a WTForm for adding a new movie with just name for the movie in it.
class NewMovie(FlaskForm):
    movie_title = StringField("What movie would you like to add?", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")

URL = "https://api.themoviedb.org/3/search/movie"
API_KEY = "94d24f9cd7dca6833897102601db0bcc"


@app.route("/add", methods=['POST', 'GET'])
def add():
    add_form = NewMovie()
    if add_form.validate_on_submit():
        movie_name = add_form.movie_title.data
        response = requests.get(URL, params={"api_key": API_KEY, "query": movie_name})
        movie_data = response.json()["results"]
        return render_template("select.html", all_results=movie_data)
    return render_template('add.html', form=add_form)


IMG_URL = "https://image.tmdb.org/t/p/w500" #This is the URL that is used for fetching images. The API returns a path that
#get added to this URL for getting the poster
@app.route("/find")
def get_movie():
    movie_id = request.args.get('id')
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    movie_data = requests.get(movie_url, params={"api_key": API_KEY, "language": "en-US"}).json()
    #And then now since I got the movie data will create a new movie object to be added in to the db
    users_movie = Movie(
            title= movie_data["title"],
            year=movie_data["release_date"].split("-")[0], #It returns year with month and date as well, used split to get rid of them
            description= movie_data["overview"],
        #The data returned for image url is a path that gets added to the API path so to get that following is done.
            img_url=f"{IMG_URL}{movie_data["poster_path"]}",
            ranking="0",
            rating="0",
            review="Change this",

    )
    db.session.add(users_movie)
    db.session.commit()
    return redirect(url_for("update", id=users_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
