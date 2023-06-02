Flask: 
  Flask is a micro web framework written in Python. 
  It is classified as a microframework because it does not require particular tools or libraries.
  We can write a function execute on web server.
  ==> It convert normal function to HTML file.
  ex:
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

  pycharm terminal:
    cmd: set FLASK_PATH=app.py #file name should be app.py if not error
    cmd2: flask run
      
  click on the ip address: 
result on webbrowser:
  browser: top right three vertical dots > more tools > Developer tools > Elements
we can see the function coverted to HTML

<html>
  <body>Hello,world</body>
</html>
