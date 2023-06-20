By using Jinja with api we can get/hold the response of any api.

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
    return  render_template("guess.html", name=name, gender=gender, age=age)

if __name__=="__main__":
    app.run(debug=True)

-------------
template/index.html

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

</body>
<footer> Current year is : {{year}} and created by Suresh Karibasa using Udemy</footer>
</html>
----------
templates/guess.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gender & Age </title>
</head>
<body>
    <h1> Hello {{name.title()}} </h1>
    <h1> I think you are {{gender}} </h1>
    <h1> And your age is {{age}} </h1>
</body>
</html>
--------------
Result:
 @http://127.0.0.1:5000/guess/hema

Hello Hema
I think you are female
And your age is 50
