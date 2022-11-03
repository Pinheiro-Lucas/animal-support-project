from flask import Blueprint
from .database import db

category = Blueprint("category", __name__)


@category.route('/create', methods=['POST'])
def create():
    # Todo: Create route
    pass


@category.route('/find', methods=['GET'])
def find_all():
    return db.find("post_category")


@category.route('/find/<idt>', methods=['GET'])
def find(idt):
    return db.find("post_category", "category_id", idt)


@category.route('/delete/<idt>', methods=['GET'])
def delete(idt):
    # Todo: Check if category is not active
    return db.update("post_category", "isActive", 0, "category_id", idt)
