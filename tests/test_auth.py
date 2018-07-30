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