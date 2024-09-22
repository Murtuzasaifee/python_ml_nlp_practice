## Jinja2 Templating Engine

'''
Varioius Jinja2 Template Syntax for reading data from data source in html file

{{  }} : expression to print output in html
{%  %} : conditions, for loops
{#  #} : this is for comments
'''


from flask import Flask, render_template,request, redirect, url_for


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

## Variable Rule

@app.route("/success/<int:score>")
def success(score):
    # return "Your marks is " + str(score)
    # return "Your marks is {}".format(score)
    #return "Your marks is %d" % score
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template("result.html", score=score, results=res)    
    

@app.route("/successres/<int:score>")
def success_result(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {"score":score,"result":res}
    
    return render_template("result1.html", results=exp)    


## IF Condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result.html", results=score)    


## Dynamic URL
@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        datascience = float(request.form["datascience"])
        
        total_score = (science + maths + c + datascience)/4
    else:
        return render_template("getresult.html")
        
    return redirect(url_for("success",score=total_score))


## Entry Point
if __name__=="__main__":
    app.run(debug=True)