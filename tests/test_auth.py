from tests.test_base import BaseClass


class TestAuthentication(BaseClass):

    def test_index_route(self):
        """ Test response for title in the index page """
        response = self.client.get('/')
        self.assertIn('Welcome to My Diary', response.data.decode())