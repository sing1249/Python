
from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('USERNAME')


posts = requests.get("https://api.npoint.io/07cbcd5039d51e959a65").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=f"Subject: Form Data\n\n "
                                                                           f"Name: {name}\n Email: {email} \n"
                                                                           f"Phone: {phone} \n Message: {message}")

        return "<h1> Form submitted successfully!"



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
