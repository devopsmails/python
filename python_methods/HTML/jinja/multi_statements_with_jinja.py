If we want to use for/any loops or if/any conditions:
  Need to use { % starting & ending at every linke of loops and conditions like %}
  ex:
server.py
=======
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask("__name__")

@app.route("/")
def home():
    random_num= random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response=requests.get(gender_url)
    gender_json = gender_response.json()
    gender = gender_json["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_json = age_response.json()
    age = age_json["age"]
    return  render_template("gender.html", name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__=="__main__":
    app.run(debug=True)

---------------
templates/blog.html
==============

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog</title>
</head>
<body>
    <!== below is the way of using LOOPS ex: for==>
    {% for blog_posts in posts: %}
        <!== below is the way of using IF conditions>
        {% if blog_posts["id"] ==2 : %}
            <h1>{{ blog_posts["title"] }}</h1>
            <h2>{{ blog_posts["subtitle"] }}</h2>
        {% endif %}
    {% endfor %}
    </body>
</html>
