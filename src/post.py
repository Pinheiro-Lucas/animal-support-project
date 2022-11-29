from flask import Blueprint, request
from .database import db

post = Blueprint("post", __name__)

"""
    "post": "post_id",
    "post_category": "category_id",
    "post_image": "post_images_id"
"""


@post.route('/', methods=['POST'])
def create():
    return db.create("post", request.json)


@post.route('/', methods=['GET'])
def find_all():
    return db.find("post")


@post.route('/<idt>', methods=['GET'])
def find(idt):
    return db.find("post", "post_id", idt)


@post.route('/<idt>', methods=['DELETE'])
def delete(idt):
    return db.delete("post", "post_id", idt)
