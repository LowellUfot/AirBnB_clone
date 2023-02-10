#!/usr/bin/python3
"""module for the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for city
       Attributes:
           state_id (string) - empty string: it will be the State.id
           name (string) - name of the state"""
    state_id = ""
    name = ""
