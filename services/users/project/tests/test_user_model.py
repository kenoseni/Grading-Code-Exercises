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
        user = add_user('parker', 'parker@gmail.com')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'parker')
        self.assertEqual(user.email, 'parker@gmail.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        """test duplicate username fails on registration"""
        add_user('parker', 'parker@gmail.com')
        duplicate_user = User(
            username='parker',
            email='parker@gmail.com'
        )
        db.session.add(duplicate_user)
        # with self.assertRaises(IntegrityError):
        #     db.session.commit()
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        """test duplicate email fails on registration"""
        add_user('parker', 'parker@gmail.com')
        duplicate_user = User(
            username='parker2',
            email='parker@gmail.com'
        )
        db.session.add(duplicate_user)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_to_json(self):
        """test to_json in model"""
        user = User(
            username='parker',
            email='parker@gmail.com'
        ).save()
        self.assertTrue(isinstance(user.to_json(), dict))
