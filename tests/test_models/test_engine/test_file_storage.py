#!/usr/bin/python3
"""
    Test module for the file_storge module
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os


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

    def test_class_instance(self):
        """tests the instance of FileStorage"""
        self.assertIsInstance(storage, FileStorage)

    def test_BaseModel_storage(self):
        """tests save and reload methods"""
        bm = BaseModel()
        bm.my_name = "John_Doe"
        bm.save()
        bm_dict = bm.to_dict()
        all_objs = storage.all()
        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def test_update(self):
        """test the update method"""
        bm = BaseModel()
        bm.my_name = "First_Name"
        bm.save()
        bm_dict = bm.to_dict()
        all_objs = storage.all()

        self.assertEqual(bm_dict['my_name'], "First_Name")

        bm.my_name = "Second_Name"
        bm.save()
        bm_dict = bm.to_dict()
        all_objs = storage.all

        self.assertEqual(bm_dict['my_name'], "Second_Name")

    def test_attribute_exist(self):
        """tests that attributes in FileStorage exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_save(self):
        """tests that objects are saved to JSON file"""
        bm = BaseModel()
        bm.my_name = "John_Doe"
        bm.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new(self):
        """Test the new method"""
        bm = BaseModel()
        var1 = bm.to_dict()
        new_key = var1['__class__'] + '.' + var1['id']
        storage.save()
        with open("file.json", 'r') as f:
            var2 = json.load(f)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])

    if __name__ == "__main__":
        unittest.main()
