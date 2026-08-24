import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("home.html")


@app.route("/predict")
def greeting():
    username = request.args.get("name")

    age_response = requests.get("https://api.agify.io", params={"name": username})
    age = age_response.json().get("age")

    gender_response = requests.get(
        "https://api.genderize.io", params={"name": username}
    )
    gender_data = gender_response.json().get("gender")

    return render_template(
        "prediction.html",
        username=username,
        age=age,
        gender=gender_data,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
