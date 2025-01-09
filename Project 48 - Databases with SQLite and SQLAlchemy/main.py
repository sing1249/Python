from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

#Initializing the SQLite extension
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

#Creating the extension.
db = SQLAlchemy(model_class=Base)

# initialize the app with the extension
db.init_app(app)

#Defining the model
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False )
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

#Creating the table
with app.app_context():
    db.create_all()

#Adding some data into the table
# with app.app_context():
#
#     data = Book(id=4, title="Zoo", author="Khaled Hosseini", rating=6)
#     db.session.add(data) #Adds the above data to the table
#     db.session.commit()





@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template('index.html', books_data=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        book = request.form["book"]  # Getting hold of the data entered in form. "name" given to each form
        # element in the form in add.html and then those names are used along with request.form to get hold of data.
        author = request.form['author']
        rating = request.form['rating']
        book_entered = Book(
                title=book,
                author=author,
                rating=rating,
        )
        with app.app_context():
            db.session.add(book_entered)  # Adds the above data to the table
            db.session.commit()

        return redirect(url_for('home'))


    return render_template('add.html')

@app.route('/edit', methods=['POST', 'GET'])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        rating_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        rating_update.rating = request.form['newrating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_to_display = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_to_display)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    with app.app_context():
        delete_book = db.get_or_404(Book, book_id)
        db.session.delete(delete_book)
        db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

