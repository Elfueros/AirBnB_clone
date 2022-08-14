#!/usr/bin/python3
""" file_storage
Defines class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Definition the class FileStorage
    It stores all instances of the program and serializes and deserializes
    them when needed

    Attributes:
        /* private class attributes */
        __file_path (str) : path to the json file
        __objects (dict) : stores the objects saved by FileStorage
        __class_list (dict) : stores all the class of the program

    Functions:
        /* Public instances methods */
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}
    __class_list = {'BaseModel': BaseModel, 'User': User, 'State': State,
                    'City': City, 'Amenity': Amenity, 'Place': Place,
                    'Review': Review}

    def all(self):
        """returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """sets in __object the object obj with the key
        <class name>.id
        """
        try:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
        except AttributeError:
            raise TypeError("Only BaseModel (sub)instances can be stored")

    def save(self):
        """serializes __objects to the json file
        """
        load_dict = {}
        for (key, value) in self.__objects.items():
            load_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(load_dict, f)

    def reload(self):
        """deserializes the json file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                load_dict = json.load(f)
            for (key, value) in load_dict.items():
                obj_class = self.__class_list[value['__class__']]
                obj = obj_class(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            #   print("JSON failed to decode the JSON file provided.")
            #   print("It's either empty or corrupted.")
            #   print("The stored data will be definitely lost at next save.")
            pass
