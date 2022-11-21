from flask import Blueprint, request
from .database import db

category = Blueprint("category", __name__)


@category.route('/', methods=['POST'])
def create():
    return db.create("post_category", request.json)


@category.route('/', methods=['GET'])
def find_all():
    return db.find("post_category")


@category.route('/<idt>', methods=['GET'])
def find(idt):
    # Todo: Find first
    return db.find("post_category", "category_id", idt)


@category.route('/<idt>', methods=['DELETE'])
def delete(idt):
    # Todo: Check if category is not active
    return db.update("post_category", "isActive", 0, "category_id", idt)
