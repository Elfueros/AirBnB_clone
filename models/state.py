#!/usr/bin/python3
"""state : Defines class State that derives from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Definition of State that inherits from Basrmodel
    Attributes:
        /* public class attributes */
        name (str) : name of the state
    """
    name = ""
