from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)


# Routes
@app.route('/')
def index():
    return render_template("base.html"), 200
