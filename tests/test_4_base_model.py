#!/usr/bin/python3
""" base_model test unit after task 4
"""
import unittest
import re
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines a test unit for the BaseModel
    Functions:
        test_init_new(self)
        test_init_kwargs(self)
        test_methods(self)
    """

    def setUp(self):
        """sets objects for the tests
        """
        self.time_pat = re.compile(
                r'^\d{4}(\-\d{2}){2}T(\d{2}:){2}\d{2}(\.\d{6})?$')
        self.uuid_pat = re.compile(
                r'^[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12}$')
        self.obj = BaseModel()
        self.obj1 = BaseModel()
        self.obj1.save()
        self.obj2 = BaseModel(**self.obj1.to_dict())
        # self.error = {'__class__': "BaseModel", 'id': 345893,
        #               'created_at': "2022:3:3T34.43.34.33444",
        #               'updated_at': "2022:3:3T34.43.34.33444"}

    def test_init_new(self):
        """tests the values initiated at an object creation
        """
        self.assertIsNotNone(self.uuid_pat.fullmatch(self.obj.id))
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertIs(self.obj.created_at, self.obj.updated_at)

    def test_init_kwargs(self):
        """tests the values initiated from a dict
        """
        # id
        self.assertIsNotNone(self.uuid_pat.fullmatch(self.obj2.id))
        # datetime patterns and unicity
        self.assertEqual(datetime, type(self.obj2.created_at))
        self.assertEqual(datetime, type(self.obj2.updated_at))
        self.assertIsNot(self.obj2.created_at, self.obj2.updated_at)
        # correspondance between orignal data and restored data
        self.assertEqual(self.obj1.id, self.obj2.id)
        self.assertEqual(self.obj1.created_at, self.obj2.created_at)
        self.assertEqual(self.obj1.updated_at, self.obj2.updated_at)
        self.assertIsNot(self.obj1, self.obj2)
        # self.assertRaise(TypeError, a = BaseModel(**self.error))

    def test_methods(self):
        """tests obj.save(), obj.__str__() and obj.to_dict for correct output
        """
        # str
        self.assertEqual("[{}] ({}) {}".format(self.obj.__class__,
                         self.obj.id, self.obj.__dict__), self.obj.__str__())
        self.assertEqual("[{}] ({}) {}".format(self.obj2.__class__,
                         self.obj2.id, self.obj2.__dict__),
                         self.obj2.__str__())
        # save
        self.assertEqual(datetime, type(self.obj1.updated_at))
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)
        # to_dict
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj1.to_dict()['created_at']))
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj1.to_dict()['updated_at']))


if (__name__ == 'main'):
    unnittest.main()
