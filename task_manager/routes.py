# IMPORTS
from flask import render_template
from task_manager import app, db


# HOMEPAGE
@app.route("/")
def home():
    return render_template("home.html")