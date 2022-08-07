#!/usr/bin/python3
""" file_storage
Defines class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json

from models.base_model import BaseModel


class FileStorage():
    """Definition the class FileStorage

    Attributes:
        /* private class attributes */
        __file_path (str) : path to the json file
        __objects (dict) : stores the objects saved by FileStorage

    Functions:
        /* Public instances methods */
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}

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
        except (AttributeError):
            raise TypeError("Only BaseModel instances can be storage.new()")

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
                obj = BaseModel(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
