# from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql

"""
    Future Stuff:
        - Use an ORM to have sql flexibility (sqlalchemy)
        - SGBD/DBMS: "Database management System", the project is using mysql-connector-python by default
        - Connection stuff is in .env file
"""

# app.config["SQLALCHEMY_DATABASE_URI"] = \
#     f"{config['DB_SYSTEM']}://" \
#     f"{config['DB_USER']}:" \
#     f"{config['DB_PASSWORD']}@" \
#     f"{config['DB_HOST']}:" \
#     f"{config['DB_PORT']}/" \
#     f"{config['DB_NAME']}"

# db = SQLAlchemy(app)


class Database:
    def __init__(self, config: dict):
        try:
            self.db = mysql.connect(
                host=config['DB_HOST'],
                port=config['DB_PORT'],
                database=config['DB_NAME'],
                user=config['DB_USER'],
                password=config['DB_PASSWORD']
            )
        except mysql.Error as err:
            # Print the problem and exit the application
            print(f"{err.errno} | {err.msg}")
            exit()

    def execute(self, command: str):
        cursor = self.db.cursor()
        # Just to avoid syntax errors
        command = command + ";" if command[-1] != ";" else command

        # Execute and commit
        cursor.execute(command)
        self.db.commit()
        cursor.close()

    def find(self, table: str, column=False, id=False):
        cursor = self.db.cursor()
        if not column and not id:
            sql = f"SELECT * FROM {table};"
        else:
            sql = f"SELECT * FROM {table} WHERE {column}={id};"

        cursor.execute(sql)

        return cursor.fetchall()

    def delete(self, table, column, info):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM %s WHERE %s = %s", (table, column, info))

        self.db.commit()
        cursor.close()
