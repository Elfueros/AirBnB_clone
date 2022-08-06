#!/usr/bin/python3
""" base_model test unit
"""
import unittest
import re
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines a test unit for the BaseModel
    Functions:
        test_init(self)
        test_methods(self)
    """

    def test_init(self):
        """tests the values initiated at an object creation
        """
        ctrl_time = datetime.now()
        obj = BaseModel()
        uuid_pat = re.compile(
                r"^[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12}$")
        self.assertIsNotNone(uuid_pat.fullmatch(obj.id))
        self.assertEqual("[BaseModel] ({}) {}".format(obj.id, obj.__dict__),
                         obj.__str__())
        self.assertEqual(type(ctrl_time), type(obj.created_at))
        self.assertIs(obj.created_at, obj.updated_at)

    def test_methods(self):
        """tests obj.save() and obj.to_dict for correct output
        """
        obj = BaseModel()
        obj.type = "appartment"
        obj.city = "Cotonou"
        obj.room = 3
        obj.area = 70
        time_pat = re.compile(
                r"^\d{4}(\-\d{2}){2}T(\d{2}:){2}\d{2}(\.\d{6})?$")
        obj.save()
        self.assertEqual(datetime, type(obj.updated_at))
        self.assertEqual(3, obj.room)
        self.assertEqual(70, obj.area)
        self.assertEqual("Cotonou", obj.city)
        self.assertEqual("appartment", obj.type)
        self.assertNotEqual(obj.created_at, obj.updated_at)
        self.assertEqual(8, len(obj.to_dict()))
        self.assertIsNotNone(time_pat.fullmatch(obj.to_dict()['created_at']))
        self.assertIsNotNone(time_pat.fullmatch((obj.to_dict())['updated_at']))
        self.assertEqual(3, obj.to_dict()['room'])
        self.assertEqual(70, obj.to_dict()['area'])
        self.assertEqual("Cotonou", obj.to_dict()['city'])
        self.assertEqual("appartment", obj.to_dict()['type'])


if (__name__ == 'main'):
    unnittest.main()
