#!/usr/bin/python3
"""
    Test module for the file_storge module
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    """Test class for the methods in class FileStorage"""

    def test_all(self):
        """tests to return all objects"""
        fs = FileStorage()
        bm = BaseModel()
        bm.my_name = "John Doe"
        bm.my_num = "89"
        bm.save()
        all_objs = fs.all()
        len_all_objs = len(all_objs)
        self.assertIsInstance(all_objs, dict)
        self.assertNotEqual(len_all_objs, 0)

    if __name__ == "__main__":
        unittest.main()
