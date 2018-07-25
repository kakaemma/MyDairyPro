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
        Adds diary object to list
        :return: 
        """

        for this_diary in DiaryModel.diary:
            if this_diary.name == self.name:
                return self.name
        DiaryModel.diary.append(self)

    @classmethod
    def get_entries(cls):
        if len(DiaryModel.diary) >=1:
            response = []
            for entry in DiaryModel.diary:
                response.append({
                'id': entry.diary_id,
                'name': entry.name,
                'Date created': entry.date_created,
                'Date Modified': entry.date_modified
                })
            return response

    @classmethod
    def get_entry(cls, diary_id):
        if len(DiaryModel.diary) >=1:
            response = []
            for entry in DiaryModel.diary:
                if entry.diary_id == diary_id:
                    response.append({
                    'id': entry.diary_id,
                    'name': entry.name,
                    'Date created': entry.date_created,
                    'Date Modified': entry.date_modified
                    })
                    return response
                return 'Entry'

        return 'Diary'












