#!/usr/bin/python3
""" base_model test unit after task 5
"""
import unittest
import re
from datetime import datetime
import json
import os

from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Defines a test unit for the BaseModel
    Functions:
        test_1_init_new(self)
        test_2_init_kwargs(self)
        test_3_str(self)
        test_4_save(self)
        test_5_to_dict(self)
        test_6_file_start(self)
        test_7_file_stored(self)
    """

    @classmethod
    def setUpClass(cls):
        """sets files and objects for tests
        """
        try:
            os.rename("file.json", "backup")
        except IOError:
            pass
        with open("file.json", "w+", encoding="utf-8") as f:
            cls.load = f.read()
        cls.time_pat = re.compile(
                r'^\d{4}(\-\d{2}){2}T(\d{2}:){2}\d{2}(\.\d{6})?$')
        cls.uuid_pat = re.compile(
                r'^[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12}$')
        cls.obj_id_pat = re.compile(
                r'BaseModel\.[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12}')
        cls.obj = BaseModel()
        cls.obj1 = BaseModel()
        cls.obj1.type = "appartment"
        cls.obj1.city = "Cotonou"
        cls.obj1.room = 3
        cls.obj1.area = 70
        cls.obj1.save()
        cls.obj2 = BaseModel(**cls.obj1.to_dict())
        with open("file.json", "r", encoding="utf-8") as f:
            cls.load_end = f.read()

    @classmethod
    def tearDownClass(self):
        """sets files back after tests
        """
        os.remove("file.json")
        try:
            os.rename("backup", "file.json")
        except IOError:
            pass

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
        self.assertIsNot(self.obj1, self.obj2)
        # correspondance between orignal data and restored data
        self.assertEqual(self.obj1.id, self.obj2.id)
        self.assertEqual(self.obj1.created_at, self.obj2.created_at)
        self.assertEqual(self.obj1.updated_at, self.obj2.updated_at)
        self.assertEqual(self.obj1.city, self.obj2.city)
        self.assertEqual(self.obj1.room, self.obj2.room)
        self.assertEqual(self.obj1.type, self.obj2.type)
        self.assertEqual(self.obj1.area, self.obj2.area)

    def test_3_str(self):
        """tests obj.__str__ for correct output
        """
        self.assertEqual("[{}] ({}) {}".format(self.obj.__class__.__name__,
                         self.obj.id, self.obj.__dict__), self.obj.__str__())
        self.assertEqual("[{}] ({}) {}".format(self.obj2.__class__.__name__,
                         self.obj2.id, self.obj2.__dict__),
                         self.obj2.__str__())

    def test_4_save(self):
        """tests obj.save for correct output
        """
        self.assertEqual(datetime, type(self.obj1.updated_at))
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)

    def test_5_to_dict(self):
        """tests obj.to_dict for correct output
        """
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

    def test_6_file_start(self):
        """tests content of file.json at creation
        """
        self.assertEqual("", self.load)

    def test_7_file_stored(self):
        """tests content of file.json after modification
        """
        self.assertEqual(len(storage.all()),
                         len(re.findall(self.obj_id_pat, self.load_end)))


if (__name__ == 'main'):
    unnittest.main()
