import datetime
from database import  DatabaseConnection

connection = DatabaseConnection()
login_id =0

class UserModel(object):


    @staticmethod
    def register_user(name, email, password):
        register_user_query = " INSERT INTO users(name, email, password) VALUES (%s,%s,%s)"
        connection.cursor.execute(register_user_query,(name, email, password))

    @staticmethod
    def check_if_user_exists_using_email(email):
        query_for_checking_email = "SELECT email FROM users WHERE email=%s"
        connection.cursor.execute(query_for_checking_email, [email])
        row = connection.cursor.fetchone()
        return row

    @staticmethod
    def check_if_is_valid_user(email, password):
        try:
            query_to_check_for_user = "SELECT user_id FROM users WHERE email=%s AND password=%s "
            connection.cursor.execute(query_to_check_for_user, (email, password))
            row = connection.cursor.fetchone()
            return row
        except Exception as exc:
            print(exc)




    @staticmethod
    def get_user_by_id(user_id):
        try:
            query_to_search_user = "SELECT user_id FROM users WHERE user_id=%s"
            connection.cursor.execute(query_to_search_user,[user_id])
            row = connection.cursor.fetchone()
            return row
        except Exception as exc:
            print(exc)



class DiaryModel(object):

    def __init__(self, name, desc, user_id):
        """
        This constructor initialises diary
        :param name: 
        """
        self.user_id = user_id
        self.name = name
        self.desc = desc
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = datetime.datetime.utcnow()

    def create_diary(self):
        """
        Adds diary entry as an object to list
        :return: 
        """

        try:
            query_to_search_diary = "SELECT * FROM entries WHERE name=%s"
            connection.cursor.execute(query_to_search_diary, [self.name])
            row = connection.cursor.fetchone()
            if row:
                return True
            query_to_add_entry = "INSERT INTO entries(name, description, user_id,date_created,date_modified) VALUES(%s,%s,%s,%s,%s)"
            connection.cursor.execute(query_to_add_entry,(self.name, self.desc, self.user_id, self.date_created, self.date_modified))
        except Exception as exc:
            print(exc)

    @classmethod
    def get_entries(cls, user_id):
        """
        This method returns all entries
        :return: 
        """
        response =[]
        query_to_get_all_entres = 'SELECT * FROM entries WHERE user_id=%s'
        connection.cursor.execute(query_to_get_all_entres,[user_id])
        rows = connection.cursor.fetchall()
        if not rows:
            return False
        for row in rows:
            response.append({
                'id': row[0],
                'name': row[1],
                'Description': row[2],
                'Date created': row[4],
                'Date Modified': row[5]
            })
        return response



    @staticmethod
    def get_entry(search_id, user_id):
        """
        This method gets a single entry
        :param diary_id: 
        :return: 
        """
        try:
            query_to_get_single_entry = "SELECT * FROM entries WHERE diary_id=%s AND user_id=%s"
            connection.cursor.execute(query_to_get_single_entry, (search_id, user_id))
            row = connection.cursor.fetchone()
            if not row:
                return False
            response =[]
            response.append({
                    'id': row[0],
                    'name': row[1],
                    'Description': row[2],
                    'Date created': row[4],
                    'Date Modified': row[5]
                })
            return response
        except Exception as exc:
            print(exc)


    @classmethod
    def modify_entry(cls, diary_id, name, desc, user_id):
        """
        This method modifies an entry
        :param diary_id: 
        :param name: 
        :param desc: 
        :return: 
        """
        query_to_search_entry = "SELECT * FROM entries WHERE diary_id=%s AND user_id=%s"
        connection.cursor.execute(query_to_search_entry, (diary_id, user_id))
        row = connection.cursor.fetchone()
        if not row:
            return False
        if row[1] == name:
            return 'update with same name'

        query_to_update = "UPDATE entries SET name=%s, description=%s WHERE user_id=%s AND diary_id=%s"
        connection.cursor.execute(query_to_update,(name,desc,user_id,diary_id))
        row_updated = connection.cursor.rowcount
        return row_updated


