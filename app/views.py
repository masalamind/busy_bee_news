from flask import render_template
from app import app

@app.route("/")
def index():
    message = "Hello Busy Bees"
    return render_template('index.html', message = message)