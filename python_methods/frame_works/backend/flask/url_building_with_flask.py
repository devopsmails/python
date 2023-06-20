From one webpage we can create an hyperlink to route to another webpage using flask
We can build an url by calling a function from .py using <a>href="" in html

Ex:
==
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

@app.route("/guess/<name>")#name is a parameter as an input
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

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts,num=num)


if __name__=="__main__":
    app.run(debug=True)

------------
templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jinja Dynamic HTML templates</title>
</head>
<body>

    <p>5*6</p>
    <!--Python code executing-->
    <p>{{5*6}}</p>
    <p>random number is : {{num}}</p>
<!--get_blog is function from server.py calling here on this webpage to go to calling function webpage with a parameter -->
<a href="{{ url_for ('get_blog',num=3)}}">Go to Blog</a>

</body>
<footer> Current year is : {{year}} and created by Suresh Karibasa using Udemy</footer>
</html>

      
