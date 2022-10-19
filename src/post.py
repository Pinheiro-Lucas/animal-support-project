from flask import Blueprint
from .database import db

post_bp = Blueprint("post", __name__)

"""
    "post": "post_id",
    "post_category": "category_id",
    "post_image": "post_images_id"
"""


@post_bp.route('/find', methods=['GET'])
def find_all():
    return db.find("post")


@post_bp.route('/find/<idt>', methods=['GET'])
def find(idt):
    return db.find("post", "post_id", idt)


@post_bp.route('/delete/<idt>', methods=['GET'])
def delete(idt):
    return db.delete("post", "post_id", idt)
