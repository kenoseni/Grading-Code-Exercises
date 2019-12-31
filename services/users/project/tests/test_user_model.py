# import unittest

from sqlalchemy.exc import IntegrityError
from database import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUsermodel(BaseTestCase):
    """Test user model"""

    def test_add_user(self):
        """test add user"""
        user = add_user('parker', 'parker@gmail.com', 'parking')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'parker')
        self.assertEqual(user.email, 'parker@gmail.com')
        self.assertTrue(user.active)
        self.assertTrue(user.password)
        self.assertFalse(user.admin)

    def test_add_user_duplicate_username(self):
        """test duplicate username fails on registration"""
        add_user('parker', 'parker@gmail.com', 'parking2')
        duplicate_user = User(
            username='parker',
            email='parker@gmail.com',
            password='parking4'
        )
        db.session.add(duplicate_user)
        # with self.assertRaises(IntegrityError):
        #     db.session.commit()
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        """test duplicate email fails on registration"""
        add_user('parker', 'parker@gmail.com', 'parking5')
        duplicate_user = User(
            username='parker2',
            email='parker@gmail.com',
            password='parking6'
        )
        db.session.add(duplicate_user)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_passwords_are_random(self):
        user_one = add_user('parker', 'parker@gmail.com', 'parking')
        user_two = add_user('parker2', 'parker2@gmail.com', 'parking')
        self.assertNotEqual(user_one.password, user_two.password)

    def test_to_json(self):
        """test to_json in model"""
        user = add_user('parker', 'parker@gmail.com', 'parking').save()
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_encode_auth_token(self):
        """"""
        user = add_user('parker', 'parker@gmail.com', 'immaculate')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        """"""
        user = add_user('parker', 'parker@gmail.com', 'parking')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)
