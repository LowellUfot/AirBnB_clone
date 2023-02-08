#!/usr/bin/python3

""" module for object storage file """
import json
from models.base_model import BaseModel


class FileStorage:
    """class for storing objects in files
    Args:
    __file_path: (string) - path to the JSON file (ex: file.json)
    __objects: (dict) - empty but will store all objects
    by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic = {k: self.__objects[k].to_dict() for k in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                obj = json.load(f)
                for key in obj.values():
                    name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(name)(**key))
        except FileNotFoundError:
            pass
