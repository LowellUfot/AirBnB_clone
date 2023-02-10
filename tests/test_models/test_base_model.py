#!/usr/bin/python3
"""
    Module to test the methods in class BaseModel
"""


import unittest
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        test class for testing BaseModel class attributes and methods
    """
    def test_uuid(self):
        """test scenario for id attribute uniquiness"""
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

    def test_created_updated_at(self):
        """test scenario of type of created_at and updated_at"""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """test scenario for the save method
            save method should update the time of the class attribute\
                    updated_at
        """
        bm = BaseModel()
        time1 = bm.updated_at
        bm.save()
        time2 = bm.updated_at
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        """test scenario for to_dict method
            checks if method returns json type
        """
        bm = BaseModel()
        dict_rep = bm.to_dict()
        self.assertIsInstance(dict_rep, dict)

    def test_base_model_instance(self):
        """test for uniqueness of the BaseModel object"""
        my_dict = dict({'my_num': 89, 'my_name': 'John_Doe'})
        bm1 = BaseModel()
        bm2 = BaseModel(**my_dict)

        self.assertIsNot(bm1, bm2)

    if __name__ == '__main__':
        unittest.main()
