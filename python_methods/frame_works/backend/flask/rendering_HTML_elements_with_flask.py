We can pass the HTML file with flask return:
app.py:
----

from flask import Flask
app = Flask(__name__)

#@.route is decorator
@app.route('/')
def hello_world():

  ##Here we can add anykind of HTML tags elements ..
  
    return '<h6 style="text-align:center"> Hello, World!</h6>'\
            '<p>This is the paragraph</p>'\
            '<img src="https://media3.giphy.com/media/mlvseq9yvZhba/giphy.gif?cid=ecf05e47pmhh20xwnjq1xg71uw0x9xs1q2eaae5skd17njwq&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>'

if __name__=="__main__":
    app.run(debug=True)
