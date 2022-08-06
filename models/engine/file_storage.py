#!/usr/bin/python3
""" file_storage
Defines class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json


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

    __file_path = "airbnb.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __object the object obj with the key
        <class name>.id
        """
        try:
            key = obj.to_dict()['__class__'] + "." + obj.id
            FileStorage.__objects[key] = obj.to_dict()
        except (AttributeError):
            raise TypeError("only BaseModel instances can be send to storage.new()")

    def save(self):
        """serializes __objects to the json file
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the json file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
