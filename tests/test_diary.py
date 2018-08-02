from tests.test_base import BaseClass


class TestDiary(BaseClass):

    def test_add_diary_without_name(self):
        """ Should return missing or bad parameters"""
        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.empty_diary,
                                    headers=self.header
                                    )
        self.assertIn('Missing or bad parameter',
                         response.data.decode())
        self.assertEqual(response.status_code, 400)



    def test_add_diary_successfully(self):
        """ should test adding entry successfully"""

        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header
                                   )
        self.assertIn('Diary successfully added', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_diary_with_wrong_version(self):
        """ Should return invalid parameters"""
        response = self.client.post('/api/v2/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header
                                   )
        self.assertIn('Invalid parameters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_diary_with_existing_name(self):
        """ Should return diary already exists"""
        self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header
                                   )
        response = self.client.post('/api/v1/entries',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header
                                    )
        self.assertIn('Diary already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)


    def test_get_diaries_on_empty_Diary(self):
        """ Should return no diary entries available"""
        response = self.client.get('/api/v1/entries', headers=self.header)
        self.assertIn('Diaries not found', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_diaries_successfully(self):
        """ Should return my diary entries"""

        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.get('/api/v1/entries', headers=self.header)
        self.assertIn('Diary entries', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_invalid_method(self):
        """ Should return Method not allowed"""

        response = self.client.post('/api/v1/entries/5',
                                    content_type='application/json',
                                    data=self.new_diary,
                                    headers=self.header
                                   )
        self.assertIn('Method not allowed', response.data.decode())
        self.assertEqual(response.status_code, 405)

    def test_get_diaries_with_wrong_version(self):
        """ Test get diary with wrong version should
        return Invalid parameters"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.get('/api/v2/entries', headers=self.header)
        self.assertIn('Invalid parameters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_single_diary_on_empty_diary(self):
        """ Should return No diary entries added"""
        response = self.client.get('/api/v1/entries/11', headers=self.header)
        self.assertIn('Entry not found',
                      response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_that_does_not_exist(self):
        """ Should return diary not found and status code 404"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.get('/api/v1/entries/2', headers=self.header)
        self.assertIn('Entry', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_single_diary_successfully(self):
        """ Should return diary not found and status code 404"""


        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.get('/api/v1/entries/1', headers=self.header)
        self.assertIn('Diary entries', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_single_diary_with_wrong_parameters(self):
        """ Should return Invalid parameters"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.get('/api/v2/entries/1', headers=self.header)
        self.assertIn('Invalid parameters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_on_empty_diary(self):
        """ Test editing when diary is empty"""
        response = self.client.put('/api/v1/entries/1',
                                   content_type='application/json',
                                   data=self.new_diary,
                                   headers=self.header
                                   )
        self.assertIn('Diary or Entry', response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_modify_diary_with_empty_name(self):
        """ Tests editing with empty values"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.put('/api/v1/entries/1',
                                   content_type='application/json',
                                   data=self.empty_diary,
                                   headers=self.header
                                   )
        self.assertIn('Missing or bad parameter submitted',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_with_wrong_id(self):
        """ Should return entry not found"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                         data=self.new_user,
                         headers=self.header)

        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.put('/api/v1/entries/2',
                                   content_type='application/json',
                                   data=self.edit_diary,
                                   headers=self.header
                                   )
        self.assertIn('Diary or Entry',
                      response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_modify_diary_with_same_name(self):
        """ Should return name exists if editing with same name"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                         data=self.new_user,
                         headers=self.header)
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.put('/api/v1/entries/1',
                                   content_type='application/json',
                                   data=self.new_diary,
                                   headers=self.header
                                   )
        self.assertIn('name already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)

    def test_modify_diary_with_wrong_parameters(self):
        """ Should return Invalid parameters"""
        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.put('/api/v2/entries/1',
                                   content_type='application/json',
                                   data=self.edit_diary,
                                   headers=self.header
                                   )
        self.assertIn('Invalid parameters', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_modify_diary_successfully(self):
        """ Should return successfully modified"""

        self.client.post('/api/v1/entries',
                         content_type='application/json',
                         data=self.new_diary,
                         headers=self.header
                         )
        response = self.client.put('/api/v1/entries/1',
                                   content_type='application/json',
                                   data=self.edit_diary,
                                   headers=self.header
                                   )
        self.assertIn('successfully modified', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        """ Test registration with missing values"""
        response = self.client.post('/api/v1/autcch/signup',
                                    content_type='application/json',
                                    data=self.empty_reg)
        self.assertIn('Please check the format of your address', response.data.decode())
        self.assertEqual(response.status_code, 404)


