from tests.test_base import BaseClass


class TestDiary(BaseClass):

    def test_add_diary_without_name(self):
        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.empty_diary,
                                    )
        self.assertIn('Missing or bad parameter submitted',
                         response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_diary_successfully(self):
        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                   )
        self.assertIn('Diary successfully added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_diary_with_existing_name(self):
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         )
        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    )
        self.assertIn('Diary already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)


    def test_get_diaries_on_empty_Diary(self):
        """ Should return no diary entries available"""
        response = self.client.get('/api/v1/entries')
        self.assertIn('Diaries not found', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_diaries_successfully(self):
        """ Should return my diary entries"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         )
        response = self.client.get('/api/v1/entries')
        self.assertIn('Diary entries', response.data.decode())
        self.assertEqual(response.status_code, 200)