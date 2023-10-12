#!/usr/bin/python3
""" This is the Base model classs"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    id:str = str(uuid4())
    created_at:datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {type(self).__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dict = self.__dict__.copy()
        dict["id"] = self.id
        dict["__class__"] = str(self.__class__.__name__)
        dict["created_at"] = self.updated_at.isoformat()
        dict["updated_at"]= self.created_at.isoformat()
        return dict

