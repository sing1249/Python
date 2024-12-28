from flask import Flask, render_template
import requests

raw_blog = requests.get("https://api.npoint.io/07cbcd5039d51e959a65").json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=raw_blog)

@app.route('/<int:blog_id>')
def get_blog(blog_id):
    current_post = None
    for posts in raw_blog:
        if posts["id"] == blog_id:
            current_post = posts
    return render_template('post.html', displayed=current_post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
