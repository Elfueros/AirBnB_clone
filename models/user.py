#!/usr/bin/python3
""" user : defines class User derived of BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Definition of class User
    It inherits from class BaseModel.
    Attributes:
        /* public class attributes */
        email (str) : email of user
        password (str) : user's password
        first_name (str) : first name of user
        last_name (str) : last name of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
