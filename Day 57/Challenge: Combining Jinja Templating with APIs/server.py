import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("home.html")


@app.route("/blog")
def blog_page():
    with open("data/blog.json") as file:
        posts = json.load(file)
        print(posts)

        return render_template("blog_posts.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
