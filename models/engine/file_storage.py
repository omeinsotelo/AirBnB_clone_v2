#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    # TODO update all
    def all(self,  cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is not None:
            objs = {}
            for key, val in self.__objects.items():
                # FIXME is no necesary this condition cls always is a class
                # if type(cls) == str:
                #     if cls == type(val).__name__:
                #         objs[key] = val
                #         continue
                if cls.__name__ == type(val).__name__:
                    objs[key] = val
            return objs
        return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    # TODO implementation delete method
    def delete(self, obj=None):
        """removes an object from __objects if it's inside
        """
        if obj is not None:
            cpy_objects = self.__objects.copy()
            instance_key = "{}.{}".format(type(obj).__name__, obj.id)
            for key in self.__objects.keys():
                if key == instance_key:
                    del cpy_objects[instance_key]
            self.__objects = cpy_objects
