#!/usr/bin/python3
"""review : Defines class Review that derives from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of Review that inherits from Basrmodel
    Attributes:
        /* public class attributes */
        place_id (str) : id of a corresponding City object
        user_id (str) : id of a corresponding User object
        text (str) : content of review
    """
    place_id = ""
    user_id = ""
    text = ""
