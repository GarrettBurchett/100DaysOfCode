from flask import Flask, render_template
import requests
from post import Post

posts = requests.get('https://api.npoint.io/bef7a6652c0027296c26').json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
