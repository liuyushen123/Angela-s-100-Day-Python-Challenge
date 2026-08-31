import json

from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post_objs = []
with open("data/data.json") as file:
    posts = json.load(file)
    for post in posts:
        # post_id, title, subtitle, body
        post_objs.append(
            Post(
                post_id=post["id"],
                subtitle=post["subtitle"],
                body=post["body"],
            )
        )


@app.route("/")
def home():
    for post in post_objs:
        print(post.subtitle)
    return render_template("index.html", posts=post_objs)


@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", post=post_objs[index - 1])


if __name__ == "__main__":
    app.run(debug=True)
