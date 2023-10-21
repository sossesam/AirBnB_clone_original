import json
import os
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()

        with open(self.__file_path, "w") as json_file:
             json.dump(dict_to_json, json_file)


    def reload(self):
        
        with open(self.__file_path, encoding="UTF-8") as myfile:
                obj_dict = json.load(myfile)
                
        for obj in obj_dict.values():
            print(obj["__class__"])
