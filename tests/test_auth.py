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

    def test_registration_with_invalid_parameters(self):
        """ Should return invalid parameters and status code 400"""
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.new_user_with_ivalid_param)
        self.assertIn('Invalid parameters',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_login_without_values(self):
        """ Should return Invalid parameters"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                                    data=self.user)
        response = self.client.post('/api/v1/auth/signup',
                                    content_type='application/json',
                                    data=self.empty_login)
        self.assertIn('Invalid parameters',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_login_with_invalid_user(self):
        """ Should return invalid user and status code 401"""

        response = self.client.post('/api/v1/auth/login',
                                    content_type='application/json',
                                    data=self.invalid_user)
        self.assertIn('Invalid user',
                      response.data.decode())
        self.assertEqual(response.status_code, 401)


    def test_successful_login(self):
        """ Test for user login successful"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                         data=self.new_user)
        response = self.client.post('/api/v1/auth/login',
                                    content_type='application/json',
                                    data=self.valid_user)
        self.assertIn('Login successful',
                      response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_successful_login_with_invalid_parameters(self):
        """Test for login with invalid parameters"""
        self.client.post('/api/v1/auth/signup',
                         content_type='application/json',
                         data=self.user)
        response = self.client.post('/api/v1/auth/login',
                                    content_type='application/json',
                                    data=self.params)
        self.assertIn('Invalid parameters',
                      response.data.decode())
        self.assertEqual(response.status_code, 400)
