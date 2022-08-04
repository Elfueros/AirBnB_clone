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


class BaseModel():
    """Definition of clas BaseModel

    Args:
        /* public instance attributes */
        id (UUID)
        created_at (time)
        updated_at (time)

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
        if (kwargs and len(kwargs) == 4):
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """updates updated_at to the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """converts self to a dictionary with a key/value pair for
        each instance attribute
        """
        return {'__class__': self.__class__, 'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()}

    def __str__(self):
        """Representation of a BaseModel object as a string
        """
        return ("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))
