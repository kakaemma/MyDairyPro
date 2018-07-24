class UserModel(object):
    """ This class handles all model operations to the User"""
    user = []

    def __init__(self, first_name, last_name, email, password):
        """
        This constructor initialises all the parameters
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        """
        self.user_id = len(UserModel.user) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password