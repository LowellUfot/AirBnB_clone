#!/usr/bin/python3
"""module for Users class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class user that inherits from the Base model
    Attributes:
        email (string): - email of the user
        password (string): - user's password
        first_name (string): - First name
        last_name (string): - Last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
