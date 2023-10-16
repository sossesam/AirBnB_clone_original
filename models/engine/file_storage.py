#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
       
        return type(self).__objects

    def new(self, obj):
       
        id = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[id] = obj

    def save(self):
        
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            new_dict = {}
            for key, val in type(self).__objects.items():
                new_dict[key] = val.to_dict()
            json.dump(new_dict, file)

    def reload(self):
      
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
