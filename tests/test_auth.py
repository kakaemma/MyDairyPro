from tests.test_base import BaseClass


class TestAuth(BaseClass):

    def test_registration_with_no_values(self):
        """ Test registration with missing values"""
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.empty_reg)
        self.assertIn('Missing values', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_registration_with_invalid_email(self):
        """ Test should return invalid email address"""
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.invalid_email)
        self.assertIn('Invalid Email address', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_registration_with_short_password(self):
        """ Should return password too short"""
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.short_password)
        self.assertIn('Unprocessable entity', response.data.decode())
        self.assertEqual(response.status_code, 422)

    def test_successful_registration(self):
        """ Should return registration successful and status code 201"""
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.new_user)
        self.assertIn('successfully added',
                      response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_registration_with_existing_email(self):
        """ Should return conflict email already exists"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                         data=self.user)
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.user)
        self.assertIn('already exists', response.data.decode())
        self.assertEqual(response.status_code, 409)