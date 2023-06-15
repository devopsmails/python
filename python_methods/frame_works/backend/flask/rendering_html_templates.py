This helps if html file is different from flask server and wants to pass the whole  HTML template to the flask server.

EX:
server.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)

------------------

index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Suresh</title>
</head>
<body>
    <h1>I'm Suresh</h1>
</body>
</html>
