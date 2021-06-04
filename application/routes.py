from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/view")
def view():
    return render_template("view.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/update")
def update():
    return render_template("update.html")
