#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
   

    def __init__(self, *args, **kwargs):
        
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if any(kwargs):
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, fmt)
                setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
       
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        
        clsName = self.__class__.__name__
        classDict = self.__dict__.copy()
        classDict['updated_at'] = self.updated_at.isoformat()
        classDict['created_at'] = self.created_at.isoformat()
        classDict['__class__'] = clsName

        return classDict

    def __str__(self):
       

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)
