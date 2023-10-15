#!/usr/bin/python3

"""pass"""

import json

class FileStorage:
    """
    pass

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key =  f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        object_dict = {}

        for key, value in self.__objects.items():
            self.__objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(object_dict, f, indent = 4)
    def reload(self):
    
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj  = json.load(f)
            for key, value in obj.items():
                self.__objects[key] = value
            print(obj)
        except FileNotFoundError:
            pass

