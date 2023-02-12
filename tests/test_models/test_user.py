#!/usr/bin/python3
"""
    Module to tests the class User
"""


import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """class to test the class User"""

    def test_user(self):
        """testing the attributes of the user class"""
        user = User()
        user.first_namme = 'John'
        user.last_name = 'Doe'
        user.email = 'john.doe@mail.com'
        user.password = 'root'
        user.save()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

if __name__ == "__main__":
    unittest.main()
