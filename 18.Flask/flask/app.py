from flask import Flask,render_template,request;

app=Flask(__name__)

@app.route("/")
def welcome1():
    return "Flask start kar diya apne, badhiya h"

@app.route("/index")
def welcome2():
    return "Aap index page par aa gaye barkhurdaar" 

@app.route("/exit")
def welcome3():
    return "Kya munna bahar nikalne ka mann h"

@app.route("/p1")
def welcome4():
    return "<html><h1> page 1 </h1></html>"

@app.route("/p2",methods=['GET'])
def welcome5():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def mfrom():
    if request.method=="POST":
        name=request.form['name']
        return (f' Hello {name} !!')
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)