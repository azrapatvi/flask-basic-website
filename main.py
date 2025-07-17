from flask import Flask,render_template # type: ignore

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html") #this will take the index.html file which is in templates folder

@app.route("/about") 
def about():
    return render_template("about.html") 

@app.route("/services") 
def services():
    return render_template("services.html")
@app.route("/contact")  
def contact():
    return render_template("contact.html") 

app.run(debug=True)