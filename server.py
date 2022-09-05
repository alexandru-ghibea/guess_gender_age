

from flask import Flask,render_template
import requests
app = Flask(__name__)


@app.route("/")
def home():
    return " Try a name and check if the age and gender matches. In the browser add the following:" \
           "/guess/insert any name here"


@app.route("/guess/<name>")
def guess(name):
    url_gender = f"https://api.genderize.io?name={name}"
    url_age = f"https://api.agify.io?name={name}"
    response_gender = requests.get(url_gender)
    response_age = requests.get(url_age)
    response_data_gender = response_gender.json()
    response_data_age = response_age.json()
    age = response_data_age["age"]
    gender = response_data_gender["gender"]
    return render_template("index.html", gender=gender, age=age, name=name)


if __name__ == "__main__":
    app.run(debug=True)
