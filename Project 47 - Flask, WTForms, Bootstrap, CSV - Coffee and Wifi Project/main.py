from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv



app = Flask(__name__) 
app.config['SECRET_KEY'] = '34r7eurfoiehf37rgwifbhf' #Any key
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time (eg 8AM)', validators=[DataRequired()])
    closing_time = StringField('Closing Time (eg 5PM)', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',choices=[("☕️"), ("☕️☕️"), ("☕️☕️☕️ ️"), ("☕️☕️☕️☕️"), ("☕️☕️☕️☕️☕️")],
                                validators=[DataRequired()])
    wifi_strength = SelectField('Wifi Strength Rating',choices=[("✘"), ("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪")],
                                validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=[("✘"), ("🔌"), ("🔌🔌"), ("🔌🔌🔌"), ("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌")] ,
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', "a", encoding='utf-8') as file: #Adding data into the csv files so users can add new cafes.
            file.write(f"\n{form.cafe.data},{form.location.data},{form.opening_time.data},{form.closing_time.data},"
                       f"{form.coffee_rating.data},{form.wifi_strength.data},{form.power_socket.data}")
        return redirect(url_for('cafes')) #This will redirect the user back to the cafes homepage by showing their data displayed.
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
