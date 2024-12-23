from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    agify = requests.get(f"https://api.agify.io?name={name}")
    age = agify.json()["age"]
    genderize = requests.get(f"https://api.genderize.io?name={name}")
    gender = genderize.json()["gender"].title()
    return render_template('age.html', name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)
