# services/users/project/tests/test_users.py

import json, unittest
from database import db
from project.api.models import User

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensures the /ping route behaves correctly"""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """Ensures a new user can be added to the database"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('michael@whoknows.org was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty""" 
        with self.client:
            response = self.client.post( '/users',
                data=json.dumps({}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'michael@whoknows.org'}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists""" 
        with self.client:
            self.client.post( 
                '/users',
                data=json.dumps({
                    'username': 'michael', 
                    'email': 'michael@whoknows.org'
                }),
                content_type='application/json'
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode()) 
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Ensure get single user behaves correctly"""
        user = User(username='michael', email='michael@whoknows.org').save()
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('michael', data['data']['username'])
            self.assertIn('michael@whoknows.org', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_all_user(self):
        """Ensure get all users behaves correctly"""
        user_1 = User(username='michael', email='michael@whoknows.org').save()
        user_2 = User(username='jackson', email='jackson@whoknows.org').save()
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('michael', data['data']['users'][0]['username'])
            self.assertIn('michael@whoknows.org', data['data']['users'][0]['email'])
            self.assertIn('jackson', data['data']['users'][1]['username'])
            self.assertIn('jackson@whoknows.org', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])


if __name__ == "__main__":
    unittest.main()
