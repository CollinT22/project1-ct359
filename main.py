import flask
import os

app = flask.Flask(__name__)

@app.route('/')  
def index(): 
    soup_list = ["Gazpacho", "Seafood Biqsue", 'Lentil Soup', "Broccoli Cheddar", "Chicken Tortilla Soup", "Tomato Soup", "Avgolemeno"]
    
    return flask.render_template("index.html", len = len(soup_list), soup_list=soup_list)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)