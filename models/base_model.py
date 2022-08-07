#!/usr/bin/python3
""" base_model: defines the class BaseModel
BaseModel is the base class of all the object of AirBnB project
It's public instance attributes are: it's id, time of creation,
and time of last update
It can update the object with current time.
It can return a dictionary containing all keys/value of the instance __dict__
"""
import uuid  # generate uuid with uuid.uuid4()
from datetime import datetime  # generate time with datetime.now()

import models


class BaseModel():
    """Definition of clas BaseModel

    Args:
        /* public instance attributes */
        id (UUID)
        created_at (time)
        updated_at (time)

        /* public class attribute */
        obj_list (list)

    Functions:
        __init__(self)

        /* public instance methods */
        save(self)
        to_dict(self)

        /* magic instance method */
        __str__(self)
    """

    def __init__(self, *args, **kwargs):
        """Initiates instance attributes
        Args:
            *args (tuple) : holds anonymous arguments
            **kwargs (dict) : holds key/values arguments
        Attributes:
            id (uuid.UUID) : id of the object
            created_at (datetime.datetime) : time of creation
            updated_at (datetime.datetime) : time of last modifications
        """
        if (kwargs and len(kwargs) >= 4):
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            for key in kwargs.keys():
                if (key not in ['__class__', 'created_at', 'updated_at']):
                    self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """updates updated_at to the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """converts self to a dictionary with a key/value pair for
        each instance attribute
        """
        result = {'__class__': self.__class__.__name__,
                  'created_at': self.created_at.isoformat(),
                  'updated_at': self.updated_at.isoformat()}
        for key in self.__dict__.keys():
            if (key not in ['created_at', 'updated_at']):
                result[key] = self.__dict__[key]
        return (result)

    def __str__(self):
        """Representation of a BaseModel object as a string
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))
