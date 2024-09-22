from flask import Flask


app = Flask(__name__)

## Home Page Route
@app.route("/")
def welcome():
    return "Welcome to My Flask Application. This is from the Home Page."

## Index Page Route
@app.route("/index")
def index():
    return "Welcome to the index page."

## Entry Point
if __name__=="__main__":
    app.run(debug=True)