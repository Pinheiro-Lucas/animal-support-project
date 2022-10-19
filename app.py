"""
- python -m flask run
- python app.py
"""

from flask import Flask, session, request, redirect, url_for, render_template, flash, current_app

from src.post import post_bp


app = Flask(__name__)

# Using flask blueprints to split code into modules
app.register_blueprint(post_bp, url_prefix="/post")


# Basic test route
@app.route('/', methods=['GET'])
def index():
    return render_template("base.html"), 200


if __name__ == "__main__":
    app.run(debug=True)  # Using debug for development
