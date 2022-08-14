#!/usr/bin/python3
"""Unit test for console command interpreter
"""
import unittest
from unittest.mock import patch
import os
import json
from io import StringIO

import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """ Definition of Unit test for command interpreter
    """

    @classmethod
    def setUpClass(self):
        """Set up test
        """
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Removes temporary file (file.json) created
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_create(self):
        """Tests output for cmd "create"
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            # creates instances for upcoming test
            self.typing.onecmd("create User")
            self.typing.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]", f.getvalue()[:7])

    def test_all(self):
        """Tests output for cmd "all"
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

    def test_destroy(self):
        """Tests output for cmd "destroy"
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_update(self):
        """Tests output for cmd "update"
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_show(self):
        """Tests output for cmd "show"
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("Any.show()")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_class_cmd(self):
        """Tests output for syntax <class>.<cmd>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(eval(f.getvalue())))


if __name__ == "__main__":
    unittest.main()
