from psycopg2 import connect,DatabaseError
from pprint import pprint

class DatabaseConnection():

    def __init__(self):
        try:
            self.connection = connect("dbname=mydiary_pro user =admin password=admin host=localhost port=5433")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Can not connect to the database")


    def create_tables(self):
        create_table_query_for_entries = (""" CREATE TABLE IF NOT EXISTS 
                                      entries(diary_id SERIAL PRIMARY KEY,
                                      name VARCHAR (15) NOT NULL, 
                                      description VARCHAR (20) NOT NULL ,
                                       user_id INTEGER NOT NULL, 
                                       date_created TIMESTAMP, 
                                       date_modified TIMESTAMP, 
                                       FOREIGN KEY (user_id)REFERENCES 
                                       users (user_id));""")

        create_table_query_for_users = ("""CREATE TABLE IF NOT EXISTS 
                    users(user_id SERIAL PRIMARY KEY,  
                    name VARCHAR(15) NOT NULL , email VARCHAR (20) NOT NULL,
                     password VARCHAR(20) NOT NULL); """
                                        )

        self.cursor.execute(create_table_query_for_entries)
        self.cursor.execute(create_table_query_for_users)

    def trancate_table(self, table_name):
        self.cursor.execute("TRUNCATE TABLE{} RESTART IDENTITY CASCADE"
                            .format(table_name))



if __name__ == '__main__':
    database_connection = DatabaseConnection()
    database_connection.create_tables()
