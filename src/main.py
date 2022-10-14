from flask import Flask, session, request, redirect, url_for, render_template, flash
from dotenv import dotenv_values

# Return a dict with everything from .env
config = dotenv_values()

app = Flask(__name__)


# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template("base.html"), 200
