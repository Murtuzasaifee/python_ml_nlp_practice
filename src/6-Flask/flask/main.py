from flask import Flask, render_template,request


app = Flask(__name__)

## Home Page Route
@app.route("/")
def welcome():
    return "<html><H1>Welcome to My Flask Application. This is from the Home Page.</H1></html>"

## Index Page Route
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

## Index Page Route
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
    
    return render_template("form.html")



@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form["name"]
        return f"Hello {name}"
    
    return render_template("form.html")

## Entry Point
if __name__=="__main__":
    app.run(debug=True)