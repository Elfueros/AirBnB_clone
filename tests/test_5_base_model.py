#!/usr/bin/python3
""" base_model and file_storage test unit after task 5
"""
import unittest
import json

from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Defines a test unit for the BaseModel
    Functions:
        test_1_first_session(self)
        test_2_second_session(self)
        test_3_third_session(self)
    """

    def setUp(self):
        """sets objects for the tests
        """
        try:
            with open("airbnb.json", "r", encoding="utf-8") as f:
                self.load = f.read()
        except FileNotFoundError:
            with open("airbnb.json", "w+", encoding="utf-8") as f:
                self.load = f.read()
        self.obj_num1 = len(storage.all())
        self.obj = BaseModel()
        self.obj.name = "zero"
        self.obj_num2 = len(storage.all())
        self.obj1 = BaseModel()
        self.obj.name = "one"
        self.obj1.type = "appartment"
        self.obj1.city = "Cotonou"
        self.obj1.room = 3
        self.obj1.area = 70
        self.obj1.save()
        self.obj_num3 = len(storage.all())

    def test_1_first_session(self):
        """checks that storage file is empty and
        the number of objects is the number created
        """
        self.assertEqual("", self.load)
        self.assertEqual(0, self.obj_num1)
        self.assertEqual(1, self.obj_num2)
        self.assertEqual(2, self.obj_num3)
        self.assertEqual(self.load, "")

    def test_2_second_session(self):
        """checks that storage file holds the json of previous session
        """
        self.assertNotEqual("", self.load)
        self.assertEqual(2, self.obj_num1)
        self.assertEqual(3, self.obj_num2)
        self.assertEqual(4, self.obj_num3)
        self.assertRegex(self.load, r"^\{\"BaseModel\.[a-f\d\-]{36}\":.+\}$")

    def test_3_third_session(self):
        """checks that storage file holds the json of previous session
        and tests correspondance with newly reloaded object
        """
        self.assertNotEqual("", self.load)
        self.assertEqual(4, self.obj_num1)
        self.assertEqual(5, self.obj_num2)
        self.assertEqual(6, self.obj_num3)
        self.assertRegex(self.load, r"^\{\"BaseModel\.[a-f\d\-]{36}\":.+\}$")


if (__name__ == 'main'):
    unnittest.main()
