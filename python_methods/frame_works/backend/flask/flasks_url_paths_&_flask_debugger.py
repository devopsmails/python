app.py
===

from flask import Flask
app = Flask(__name__)

#@.route is decorator
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def goodbye():
    return 'Bye!Bye!'

@app.route('/home')
def welcome():
    return 'Welcome my friend!'
#type1
#@app.route('/<name>')
#type2
#@app.route('/username/<name>')
#type3
#@app.route('/username/<name>/1')
#type4
#@app.route('/username/<name>/1')
#type5(converter)#what ever the string we add after the path / then it shows as path
@app.route("/username/<name>/<int:number>")
def greet(name):
    return f"Hello Mr. {name}, you are {number} years old "

if __name__=="__main__":
    # if we get a type error as concatenating string + int.
    #we can auto reload
    # We can directly fix on the website by click on right down black debug symbol fix there
    app.run(debug=True)
Results:
--------
pycharm: terminal >:
set FLASK_PATH=app.py
flask run
 >> get link > click link: That's the above code results
  
