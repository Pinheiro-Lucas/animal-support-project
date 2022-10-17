"""
- python -m flask run
- python app.py
"""

from flask import Flask, session, request, redirect, url_for, render_template, flash, current_app
from dotenv import dotenv_values
from src.database import Database

# Return a dict with everything from .env
config = dotenv_values()

db = Database(config)
app = Flask(__name__)


# Routes
@app.route('/', methods=['GET'])
def index():
    return render_template("base.html"), 200


@app.route('/find/<table>', methods=['GET'])
def find_all(table):
    return db.find(table)


@app.route('/find/<table>/<idt>', methods=['GET'])
def find(table, idt):
    ids = {
        "post": "post_id",
        "post_category": "category_id",
        "post_image": "post_images_id"
    }

    return db.find(table, ids[table], idt)


@app.route('/delete/<table>/<idt>', methods=['GET'])
def find(table, idt):
    ids = {
        "post": "post_id",
        "post_category": "category_id",
        "post_image": "post_images_id"
    }

    return db.find(table, ids[table], idt)


if __name__ == "__main__":
    app.run()
