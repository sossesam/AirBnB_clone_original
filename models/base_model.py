#!/usr/bin/python3
""" This is the Base model classs"""

from uuid import uuid4
from datetime import datetime
from models import storage

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
            storage.new(self)


    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()
        
    
    def to_dict(self):
        dict = self.__dict__.copy()
        dict["id"] = self.id
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.updated_at.isoformat()
        dict["updated_at"]= self.created_at.isoformat()

        return dict

