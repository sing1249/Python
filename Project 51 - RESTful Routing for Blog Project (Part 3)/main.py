from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from time import strftime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

#Showing all posts.
@app.route('/')
def get_all_posts():
    # Querying the database for all the posts. Converting the data to a python list.
    with app.app_context():
        posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

#Showing a specific post when user clicks on it.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


#Creating the form for new post using CKEditor for body.
ckeditor = CKEditor(app) #Initilaizing CKEditor
class MyForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    name = StringField("Your Name", validators=[DataRequired()])
    url =  StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Body of the blog", validators=[DataRequired()])
    submit = SubmitField(label="Add Blog")


#Creating new post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    new_blog = MyForm()
    if new_blog.validate_on_submit():
        #Create a new object for the db.
        new_post = BlogPost(
            title = new_blog.title.data,
            subtitle = new_blog.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            body = new_blog.body.data,
            author = new_blog.name.data,
            img_url = new_blog.url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts")) #Returns to the homepage with all blogs.

    return render_template("make-post.html", form=new_blog)

#Editing the posts
@app.route("/edit-post/<int:post_id>", methods = ['GET', 'POST'])
def edit_post(post_id):
    current_post = db.get_or_404(BlogPost, post_id)
    edit_form = MyForm(
        title = current_post.title,
        subtitle = current_post.subtitle,
        name = current_post.author,
        url = current_post.img_url,
        body = current_post.body,
    )

    if edit_form.validate_on_submit():
        current_post.title = edit_form.title.data #Gets hold of data from the form and update them for current post selected.
        current_post.subtitle = edit_form.subtitle.data
        current_post.body = edit_form.body.data
        current_post.author = edit_form.name.data
        current_post.img_url = edit_form.url.data

        db.session.commit()
        return redirect(url_for("show_post", post_id=current_post.id)) #Will redirect to the current post that is being edited using post id
    return render_template("make-post.html", form=edit_form, editing = True) #Passing editing = True to get customized headings.


# Deleting a post from the database.
@app.route("/delete/<int:post_id")
def delete_post(post_id):
    post_to_be_deleted = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_be_deleted)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
