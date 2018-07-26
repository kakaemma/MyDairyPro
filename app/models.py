import datetime


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
        Adds diary entry as an object to list
        :return: 
        """

        for this_diary in DiaryModel.diary:
            if this_diary.name == self.name:
                return self.name
        DiaryModel.diary.append(self)

    @classmethod
    def get_entries(cls):
        """
        This method returns all entries
        :return: 
        """
        if len(DiaryModel.diary) >= 1:
            response = []
            for entry in DiaryModel.diary:
                response.append({
                    'id': entry.diary_id,
                    'name': entry.name,
                    'Description': entry.desc,
                    'Date created': entry.date_created,
                    'Date Modified': entry.date_modified
                })
            return response

    @staticmethod
    def get_entry(search_id):
        """
        This method gets a single entry
        :param diary_id: 
        :return: 
        """
        if len(DiaryModel.diary) >= 1:
            response = []
            for entry in DiaryModel.diary:
                if entry.diary_id == search_id:
                    response.append({
                            'id': entry.diary_id,
                            'name': entry.name,
                            'Description': entry.desc,
                            'Date created': entry.date_created,
                            'Date Modified': entry.date_modified
                        })

            return response
        return 'Diary'

    @classmethod
    def modify_entry(cls, diary_id, name, desc):
        """
        This method modifies an entry
        :param diary_id: 
        :param name: 
        :param desc: 
        :return: 
        """
        if len(DiaryModel.diary) >= 1:

            for entry in DiaryModel.diary:
                if entry.diary_id == diary_id:
                    if entry.name == name:
                        return 'same name'
                    entry.name = name
                    entry.dec = desc
                    entry.date_modified = datetime.datetime.utcnow()
                    return 'modified'
