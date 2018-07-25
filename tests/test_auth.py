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
        self.assertIn('Missing or bad parameter submitted', response.data.decode())


    def test_registration_with_invalid_email(self):
        """ Test should return invalid email address"""
        response = self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.invalid_email)
        self.assertIn('Unprocessable entity', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_registration_with_short_password(self):
        """ Should return password too short"""
        response = self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.short_password)
        self.assertIn('Password too short', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_successful_registration(self):
        """ Should return registration successful and status code 201"""
        response = self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.user)
        self.assertIn('successfully registered',
                      response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_registration_with_existing_email(self):
        """ Should return conflict email already exists"""
        self.client.post('/api/v1/register',
                         content_type='application/json',
                         data=self.user)
        response = self.client.post('/api/v1/register',
                                    content_type='application/json',
                                    data=self.user)
        self.assertIn('email already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)
