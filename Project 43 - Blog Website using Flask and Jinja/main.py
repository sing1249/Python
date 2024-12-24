from flask import Flask, render_template
import requests
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_elements = []
for post in posts:
    #Passing the arguments into the Post class to create a new object for each post
    new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_elements.append(new_post)

# print(post_elements)
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_elements)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    requested_post = None
    #Checks for all posts in the objects that were created using class.
    for requested in post_elements:
        #If the requested blog id by user is same as post id, it will then make that post as the requested post.
        #And then when rendering post.html, we can loop in the requested post and get elements displayed.
        if requested.id == blog_id:
            requested_post = requested
    return render_template("post.html", current_post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
