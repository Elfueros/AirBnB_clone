#!/usr/bin/python3
""" user test unit
"""
import unittest
import re
import os

from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """Defines a test unit for the User
    Functions:
        test_0_class_attr(self)
        test_1_reload(self)
        test_2_new(self)
        test_3_new_save(self)
        test_4_save(self)
    """

    @classmethod
    def setUpClass(cls):
        """sets files and objects for tests
        """
        # read existing json or create json storage file
        try:
            with open("file.json", "r", encoding="utf-8") as f:
                cls.load_start = f.read()
            os.rename("file.json", "backup")
        except FileNotFoundError:
            cls.load_start = ""
            pass
        with open("file.json", "w+", encoding="utf-8") as f:
            cls.load = f.read()
        # regex pattern
        cls.obj_id_pat = re.compile(
                r'(User\.[\da-f]{8}(\-[\da-f]{4}){3}\-[\da-f]{12})')
        # set of keys from json file and from storage object
        cls.load_start = [i[0] for i in cls.obj_id_pat.findall(cls.load_start)]
        cls.start_keys = storage.all().keys()
        # create objects
        cls.obj1 = User()
        cls.obj1.email = "lenal@lcorp.com"
        cls.obj1.area = 70
        cls.obj1.save()
        cls.obj2 = User()
        cls.obj3 = User(**cls.obj2.to_dict())
        storage.save()
        # set of keys from json file at the end
        with open("file.json", "r", encoding="utf-8") as f:
            cls.load_end = f.read()
        cls.end_keys = [i[0] for i in re.findall(cls.obj_id_pat, cls.load_end)]

    @classmethod
    def tearDownClass(self):
        """sets files back after tests
        """
        os.remove("file.json")
        try:
            os.rename("backup", "file.json")
        except IOError:
            pass

    def test_1_reload(self):
        """tests the values initiated at an object deserialization
        (obj.__init__ storage.all and storage.reload)
        """
        for i in range(0, len(self.load_start)):
            self.assertIn(self.load_start[i], self.start_keys)

    def test_2_new(self):
        """tests storage.new arguments
        """
        with self.assertRaises(AttributeError):
            storage.new(None)
        with self.assertRaises(AttributeError):
            storage.new(23.45)
        with self.assertRaises(AttributeError):
            storage.new("23.45")

    def test_3_new_save(self):
        """tests storage.new actions
        """
        self.assertIn("User." + self.obj1.id, self.end_keys)
        self.assertIn("User." + self.obj2.id, self.end_keys)
        self.assertEqual(self.end_keys.count("User." + self.obj3.id), 1)

    def test_4_save(self):
        """tests obj.save and storage.save
        """
        self.assertEqual(len(storage.all()),
                         len(re.findall(self.obj_id_pat, self.load_end)))

    def test_0_class_attr(self):
        """checks the value of class attributes
        """
        with self.assertRaises(AttributeError):
            storage.__file_path == "file.json"
        with self.assertRaises(AttributeError):
            storage.__objects == {}


if (__name__ == 'main'):
    unnittest.main()
