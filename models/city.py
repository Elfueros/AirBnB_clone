#!/usr/bin/python3
"""city : Defines class City that derives from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of City that inherits from Basrmodel
    Attributes:
        /* public class attributes */
        name (str) : name of the city
        state_id (str) : id of a corresponding State obect
    """
    name = ""
    state_id = ""
