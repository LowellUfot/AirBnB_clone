#!/usr/bin/python3
"""module for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for review"""
    place_id = ""
    user_id = ""
    text = ""
