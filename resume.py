from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app1 = Flask(__name__)

@app1.route("/about")
def about():
    return render_template('index.html')

@app1.route("/experience")
def exp():
    return render_template('experience.html')

@app1.route("/education")
def edu():
    return render_template('education.html')

@app1.route("/skills")
def skills():
    return render_template('skills.html')

@app1.route("/interests")
def interests():
    return render_template('interests.html')

@app1.route("/awards")
def awards():
    return render_template('awards.html')

@app1.route("/Publications")
def publications():
    return render_template('publications.html')


app1.run(debug=True)
