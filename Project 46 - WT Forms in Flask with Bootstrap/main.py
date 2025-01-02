from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5



class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(check_deliverability=True, message="Missing @ in email!")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Minimum 8 required.")])
    submit = SubmitField(label='Login')


app = Flask(__name__)

app.secret_key = 'sfhdkfkjsdfkjsdfkjsdf'
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit(): #Form will be submitted if it is validated, so only getting hold of data at that time.
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            print("valid")
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
