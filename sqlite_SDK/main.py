import sqlite3


class Database:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?) ", (user_id,))


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(result))


    # HERE YOU CAN ADD MORE FUNCTIONALITY TO YOUR SQL SDK BY ADDING MORE PROCEDURE 
    # WITH RAW SQL QUERIES.
