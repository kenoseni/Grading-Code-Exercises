# services/users/project/tests/test_users.py

import unittest
import json

from database import db
from project.api.models import User
from project.tests.utils import add_user, add_admin
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

        add_admin('test', 'test@test.org', 'test')
        
        with self.client:
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps({
                    'email': 'test@test.org',
                    'password': 'test'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org',
                    'password': 'mickky'
                }),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('michael@whoknows.org was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_not_admin(self):
        add_user('test', 'test@test.org', 'test')
        with self.client:
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps({
                    'email': 'test@test.org',
                    'password': 'test'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org',
                    'password': 'mickky'
                }),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'You do not have permission to do that.'
            )
            self.assertEqual(response.status_code, 401)


    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty"""
        add_admin('test', 'test@test.org', 'test')
        with self.client:
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps({
                    'email': 'test@test.org',
                    'password': 'test'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object
        does not have a username key"""
        add_admin('test', 'test@test.org', 'test')
        with self.client:
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps({
                    'email': 'test@test.org',
                    'password': 'test'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'michael@whoknows.org'}),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email already exists"""
        add_admin('test', 'test@test.org', 'test')
        resp_login = self.client.post(
            '/auth/login',
            data=json.dumps({
                'email': 'test@test.org',
                'password': 'test'
            }),
            content_type='application/json'

        )
        token = json.loads(resp_login.data.decode())['auth_token']
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org',
                    'password': 'mickky4'
                }),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org',
                    'password': 'mickky5'
                }),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_inactive(self):
        add_user('michael', 'michael@whoknows.org', 'mickky7')
        # update user
        user = User.query.filter_by(email='michael@whoknows.org').first()
        user.active = False
        db.session.commit()
        with self.client:
            # user login
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps({
                    'email': 'michael@whoknows.org',
                    'password': 'mickky7'
                }),
                content_type='application/json'
            )
            token = json.loads(resp_login.data.decode())['auth_token']
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'michael',
                    'email': 'michael@whoknows.org',
                    'password': 'mickky7'
                }),
                content_type='application/json',
                headers={'Authorization': f'Bearer {token}'}
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Provide a valid auth token')
            self.assertEqual(response.status_code, 401)

    def test_single_user(self):
        """Ensure get single user behaves correctly"""
        user = add_user('michael', 'michael@whoknows.org', 'mickky7')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('michael', data['data']['username'])
            self.assertIn('michael@whoknows.org', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_all_user(self):
        """Ensure get all users behaves correctly"""
        add_user('michael', 'michael@whoknows.org', 'mickky9')
        add_user('jackson', 'jackson@whoknows.org', 'jakky')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('michael', data['data']['users'][0]['username'])
            self.assertIn(
                'michael@whoknows.org', data['data']['users'][0]['email'])
            self.assertIn('jackson', data['data']['users'][1]['username'])
            self.assertIn(
                'jackson@whoknows.org', data['data']['users'][1]['email'])
            self.assertFalse(data['data']['users'][1]['admin'])
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        """Ensures the mail route behaves correctly when no users have been
        added to the database"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>No users!</p>', response.data)

    def test_main_with_users(self):
        """Ensures the mail route behaves correctly when no users have been
        added to the database"""
        User(
            username='michael',
            email='michael@whoknows.org',
            password='babajide').save()
        User(
            username='jackson',
            email='jackson@whoknows.org',
            password='babajide2').save()
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>All Users</h1>', response.data)
            self.assertNotIn(b'<p>No users!</p>', response.data)
            self.assertIn(b'michael', response.data)
            self.assertIn(b'jackson', response.data)

    def test_main_add_user(self):
        """Ensures a new user can be added to the database"""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(username='gbenga', email='gbenga@gmail.com', password='gbengs'),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>All Users</h1>', response.data)
            self.assertNotIn(b'<h1>No Users</h1>', response.data)
            self.assertIn(b'gbenga', response.data)


if __name__ == "__main__":
    unittest.main()
