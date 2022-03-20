from flask import render_template, url_for, request
from flaskapp import app, db
from flaskapp.static.python import main

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/bank")
def bank():
    return render_template('bank.html', title='Banks and Branches')

@app.route("/branch/<count>")
def produce_branch(count):
    main.create_branches(count)