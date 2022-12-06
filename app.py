"""
- python -m flask run
- python app.py
"""

from flask import Flask, session, request, redirect, url_for, render_template, flash, current_app
from flask_cors import CORS

from src.database import config
from src.post import post
from src.category import category


app = Flask(__name__)
# Access-Control-Allow-Origin
CORS(app)  # Cross Origin Resource Sharing

# Using flask blueprints to split code into modules
app.register_blueprint(post, url_prefix="/post")
app.register_blueprint(category, url_prefix="/category")


# Basic test route
@app.route('/', methods=['GET'])
def index():
    return render_template("base.html"), 200


if __name__ == "__main__":
    app.run(debug=True, port=config["PORT"])  # Using debug for development
