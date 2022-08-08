#!/usr/bin/python3
"""amenity : Defines class Amenity that derives from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Definition of Amenity that inherits from Basrmodel
    Attributes:
        /* public class attributes */
        name (str) : name of the city
    """
    name = ""
