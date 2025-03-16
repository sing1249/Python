from datetime import date
from enum import unique

from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app) #Initializing the Login

#User Load back callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

#Adding the profile images for the comments section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))# Foreign Key - Establishes the relationship to the User table
    author = relationship("User", back_populates="posts") #If a `BlogPost` object has `author_id = 1`, SQLAlchemy will automatically fetch the `User` whose `id = 1`.
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post") #Parent relationship

#Creating the user table
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    posts = relationship("BlogPost", back_populates="author") # Relationship - Links User to BlogPost
    comments = relationship("Comment", back_populates="comment_author") #Adding relationship, comment author is in comments class.

#Creating the comments table
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer,
                                           ForeignKey("users.id"))  # Correct ForeignKey reference to users table
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("blog_posts.id"))  # ForeignKey to BlogPost table

    comment_author = relationship("User", back_populates="comments")  # Links Comment to User
    parent_post = relationship("BlogPost", back_populates="comments")  # Links Comment to BlogPost

    text: Mapped[str] = mapped_column(Text, unique=False, nullable=False)

with app.app_context():
    db.create_all()


#Using Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_name = register_form.name.data
        user_email = register_form.email.data
        user_password = register_form.password.data
        hashed_password = generate_password_hash(user_password, method="pbkdf2:sha256", salt_length=8)
        checking_user = db.session.execute(db.select(User).where(User.email==user_email)).scalar()
        if checking_user:
            flash("You are already registered. Please login using your email and password")
            return redirect(url_for("login"))
        else:
            registering = User(
                name = user_name,
                email = user_email,
                password = hashed_password,
            )

            db.session.add(registering)
            db.session.commit()
            login_user(registering) #Logging in the user as soon as they register
            return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=register_form, current_user=current_user)


#Retrieves a user from the database based on their email.
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_email = login_form.email.data
        user_password = login_form.password.data
        # Now to check if the user is in db, finding the user in db using the email they entered.
        user_object_in_db = db.session.execute(db.select(User).where(User.email==user_email)).scalar()
        if not user_object_in_db:
            flash("User not in the database. Please register")
            return redirect(url_for("register"))
        elif not check_password_hash(pwhash=user_object_in_db.password, password=user_password):
            flash("Incorrect password. Try again.")
            return redirect(url_for("login"))
        else:
            login_user(user_object_in_db) #Logs in user if the password is correct.
            return redirect(url_for("get_all_posts"))
    return render_template("login.html", form=login_form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    #Getting the users to comment
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please login/register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)

#Creating the decorator function for admin only access.
def admin_only(f):
    @wraps(f) #Gets the name of the function being decorated and keeps all of its data
    def decorated_function(*args, **kwargs): #Creating the decorator
        if current_user.id != 1: #Checking is the current_user's id is not 1
            return abort(403) #If it is not 1 then it will return error code 403.
        else:
            return f(*args, **kwargs) #Else it will execute the f (the function being passed to the decorator) with any args or kwargs given as well.

    return decorated_function


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
