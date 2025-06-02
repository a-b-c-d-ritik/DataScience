from flask import Flask;

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


if __name__=="__main__":
    app.run(debug=True)