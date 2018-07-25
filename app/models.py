import datetime


class UserModel(object):
    """ This class handles all model operations to the User"""
    users = []

    def __init__(self, name, email, password):
        """
        This constructor initialises all the parameters
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        """
        self.user_id = len(UserModel.users) + 1
        self.name = name
        self.email = email
        self.password = password

    def add_user(self):
        for user in UserModel.users:
            if user.email == self.email:
                return 'exists'
        UserModel.users.append(self)

class DiaryModel(object):
    diary = []

    def __init__(self, name, desc):
        """
        This constructor initialises diary
        :param name: 
        """
        self.diary_id = len(DiaryModel.diary)+1
        self.name = name
        self.desc = desc
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_diary(self):
        """
        Adds diary object to list
        :return: 
        """
        DiaryModel.diary.append(self)
        return self.diary_id




