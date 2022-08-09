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
        test_1_init_new(self)
        test_2_init_kwargs(self)
        test_3_methods(self)
    """

    @classmethod
    def setUpClass(cls):
        """sets objects for the tests
        """
        cls.time_pat = re.compile(
                r'^\d{4}(\-\d{2}){2}T(\d{2}:){2}\d{2}(\.\d{6})?$')
        cls.uuid_pat = re.compile(
                r'^[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12}$')
        cls.obj = BaseModel()
        cls.obj1 = BaseModel()
        cls.obj1.type = "appartment"
        cls.obj1.city = "Cotonou"
        cls.obj1.room = 3
        cls.obj1.area = 70
        cls.obj1.save()
        cls.obj2 = BaseModel(**cls.obj1.to_dict())
        # cls.error = {'__class__': "BaseModel", 'id': 345893,
        #               'created_at': "2022:3:3T34.43.34.33444",
        #               'updated_at': "2022:3:3T34.43.34.33444"}

    def test_1_init_new(self):
        """tests the values initiated at an object creation
        """
        self.assertIsNotNone(self.uuid_pat.fullmatch(self.obj.id))
        self.assertEqual(datetime, type(self.obj.created_at))
        self.assertIs(self.obj.created_at, self.obj.updated_at)

    def test_2_init_kwargs(self):
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
        self.assertEqual(self.obj1.city, self.obj2.city)
        self.assertEqual(self.obj1.room, self.obj2.room)
        self.assertEqual(self.obj1.type, self.obj2.type)
        self.assertEqual(self.obj1.area, self.obj2.area)
        self.assertIsNot(self.obj1, self.obj2)
        # self.assertRaise(TypeError, a = BaseModel(**self.error))

    def test_3_methods(self):
        """tests obj.save(), obj.__str__() and obj.to_dict for correct output
        """
        # str
        self.assertEqual("[{}] ({}) {}".format(self.obj.__class__.__name__,
                         self.obj.id, self.obj.__dict__), self.obj.__str__())
        self.assertEqual("[{}] ({}) {}".format(self.obj2.__class__.__name__,
                         self.obj2.id, self.obj2.__dict__),
                         self.obj2.__str__())
        # save
        self.assertEqual(datetime, type(self.obj1.updated_at))
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)
        # to_dict
        self.assertEqual(8, len(self.obj1.to_dict()))
        self.assertEqual(3, self.obj1.to_dict()['room'])
        self.assertEqual(70, self.obj1.to_dict()['area'])
        self.assertEqual("Cotonou", self.obj1.to_dict()['city'])
        self.assertEqual("appartment", self.obj1.to_dict()['type'])
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj1.to_dict()['created_at']))
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj1.to_dict()['updated_at']))

        self.assertEqual(8, len(self.obj2.to_dict()))
        self.assertEqual(3, self.obj2.to_dict()['room'])
        self.assertEqual(70, self.obj2.to_dict()['area'])
        self.assertEqual("Cotonou", self.obj2.to_dict()['city'])
        self.assertEqual("appartment", self.obj2.to_dict()['type'])
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj2.to_dict()['created_at']))
        self.assertIsNotNone(self.time_pat.fullmatch(
            self.obj2.to_dict()['updated_at']))


if (__name__ == 'main'):
    unnittest.main()
