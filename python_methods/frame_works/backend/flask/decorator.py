Decorator:
  Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
  Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
  
ex:
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
