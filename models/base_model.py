import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_data = self.__dict__.copy()
        dict_data["__class__"] = self.__class__.__name__
        dict_data["created_at"] = self.created_at.isoformat()
        dict_data["updated_at"] = self.updated_at.isoformat()
        return dict_data


