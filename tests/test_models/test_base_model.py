#!/usr/bin/python3
"""
    Module to test the methods in class BaseModel
"""


import unittest
from models.BaseModel import BaseModel


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
        self.assetNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

    def test_created_updated_at(self):
        """test scenarion of type of created_at and updated_at"""
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
        bm.save
        time2 = bm.updated_at
        self.assertIsNotEqual(time1, time2)

    def test_to_dict(self):
        """test scenario for to_dict method
            checks if method returns json type
        """
        bm = BaseModel()
        json_string = bm.to_dict
        python_string = json.loads(json_string)
        self.assertIsInstance(python_string, dict)

    if __name__ == '__main__':
        unittest.main()
