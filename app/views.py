from flask import render_template
from app import app

@app.route("/")
@app.route("/home")
def home():
    message = "Hello Busy Bees"
    return render_template('home.html', message = message)