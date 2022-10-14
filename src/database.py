from flask_sqlalchemy import SQLAlchemy
from main import app, config

"""
    Important Stuff:
        - Using sqlalchemy to have sql flexibility (ORM)
        - SGBD/DBMS: "Database management System", the project is using mysql-connector-python by default
        - Connection stuff is in .env file
        - URI: Identifies a resource
"""

app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"{config['DB_SYSTEM']}://" \
    f"{config['DB_USER']}:" \
    f"{config['DB_PASSWORD']}@" \
    f"{config['DB_HOST']}:" \
    f"{config['DB_PORT']}/" \
    f"{config['DB_NAME']}"


db = SQLAlchemy(app)

# Todo: Tables
