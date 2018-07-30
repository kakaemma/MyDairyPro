from psycopg2 import connect
from pprint import pprint

class DatabaseConnection():

    def __init__(self):
        try:
            self.connection = connect("dbname=postgres user =postgres password=123456 host=localhost port=5433")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("success")
        except:
            pprint("Can not connect to the database")

    def create_table_users(self):
        create_table_query_for_users = ("""CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,  name VARCHAR(15) NOT NULL , email VARCHAR (20) NOT NULL, password VARCHAR(20) NOT NULL); """ )
        self.cursor.execute(create_table_query_for_users)

if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_table_users()











