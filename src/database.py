# from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql
from dotenv import dotenv_values

"""
    Future Stuff:
        - Use an ORM to have sql flexibility (sqlalchemy)
        - SGBD/DBMS: "Database management System", the project is using mysql-connector-python by default
        - Connection stuff is in .env file
"""

# app.config["SQLALCHEMY_DATABASE_URI"] = \
#     f"{config['DB_CONNECTION']}://" \
#     f"{config['DB_USER']}:" \
#     f"{config['DB_PASSWORD']}@" \
#     f"{config['DB_HOST']}:" \
#     f"{config['DB_PORT']}/" \
#     f"{config['DB_NAME']}"

# db = SQLAlchemy(app)


class Database:
    def __init__(self, cfg):
        try:
            self.db = mysql.connect(
                host=cfg['DB_HOST'],
                port=cfg['DB_PORT'],
                database=cfg['DB_NAME'],
                user=cfg['DB_USER'],
                password=cfg['DB_PASSWORD']
            )
        except mysql.Error as err:
            # Print the problem and exit the application
            print(f"{err.errno} | {err.msg}")
            exit()

    def execute(self, command):
        cursor = self.db.cursor()
        # Just to avoid syntax errors
        command = command + ";" if command[-1] != ";" else command

        # Execute and commit
        cursor.execute(command)
        self.db.commit()
        cursor.close()

    def find(self, table, column=False, id=False):
        cursor = self.db.cursor()
        if not column and not id:
            sql = f"SELECT * FROM {table};"
        else:
            sql = f"SELECT * FROM {table} WHERE {column}={id};"

        cursor.execute(sql)

        return cursor.fetchall()

    def delete(self, table, column, info):
        cursor = self.db.cursor()

        sql = f"DELETE FROM {table} WHERE {column}={info}"

        cursor.execute(sql)

        self.db.commit()
        cursor.close()

        # Todo: Check if post exists (return 404)
        return "200"  # Just for tests


# Return a dict with everything from .env
config = dotenv_values()

db = Database(config)
