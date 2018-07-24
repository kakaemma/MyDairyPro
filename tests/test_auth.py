from tests.test_base import BaseClass


class TestAuthentication(BaseClass):

    def test_index_route(self):
        """ Test response for title in the index page """
        response = self.client.get('/')
        self.assertIn('Welcome to My Diary', response.data.decode())

    def test_registration_with_no_values(self):
        """ Test registration with missing values"""
        response = self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.empty_reg)
        self.assertIn('Missing values', response.data.decode())
