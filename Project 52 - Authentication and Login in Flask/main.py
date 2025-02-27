from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'se5y4wewt233wtvw3t'




class Base(DeclarativeBase):
    pass

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#Initializing login manager
login_manager = LoginManager()
login_manager.init_app(app)

#User Load back callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id) #Getting the user_id from the db as it takes the str ID of a user, and return the corresponding user object.



# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated) #logged_in is passed to check if the current_user is alreayd logged in (authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_email = request.form.get("email")
        find_user = db.session.execute(db.select(User).where(User.email==user_email)).scalar()
        if find_user:
            flash("This email is already registered. Please login with your password")
            return redirect(url_for("login"))
        else:
            user_name = request.form.get("name")
            hashed_password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
            new_user_created = User(
                email = user_email,
                password = hashed_password,
                name = user_name,
            )
            db.session.add(new_user_created)
            db.session.commit()

            #Logging the user using login_user() after they are registered.
            login_user(new_user_created)
            return redirect(url_for("secrets", name=user_name))

    return render_template("register.html", logged_in=current_user.is_authenticated)


#Configuring the Login route
# first step would be to check if the user is doing a post request
# Get hold of the user's email and password they entered
# Find the email that user entered in the form in db using where clause
# After the user is found, get the object and then get hashed password stored in db and then use check_password_hash method
# with password entered and then render the template if the password matches.
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        users_email = request.form.get("email")
        users_password = request.form.get("password")
        #Locating the user with the email in db
        user_result = db.session.execute(db.select(User).where(User.email==users_email))
        user_object = user_result.scalar()
        if not user_object:
            flash("No account associated with this email.")
            return redirect(url_for("login"))
        elif not check_password_hash(pwhash=user_object.password, password=users_password):
            flash("Incorrect password")
            return redirect(url_for("login"))
        else:
            login_user(user_object)
            return redirect(url_for("secrets")) #Once the login is successful it will take to secrets page
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required #Using this so that user is logged in before accessing this route.
def secrets():
    #To display the users name, current_user is used, gets access to current user and then their name.
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required #Using this so that user is logged in before accessing this route.
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
