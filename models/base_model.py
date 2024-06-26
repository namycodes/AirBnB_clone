#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
import models


# base class component
class BaseModel:

    # class constructor/initializer
    def __init__(self, **kwargs):

        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    ''' 
        returns the string representation of the class
    '''

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    '''
        assigns the current time to the update_at and returns it 
    '''

    def save(self):
        if self.updated_at:
            self.updated_at = datetime.now()
            models.storage.save()
        return self.updated_at

    ''' 
        returns the dictionary representation of the class 
    '''

    def to_dict(self):
        new_dict = {}
        if self.__dict__:
            new_dict.update(self.__dict__)
            new_dict['__class__'] = self.__class__.__name__
            new_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            new_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            return new_dict
        else:
            return "Error: Instance has no attributes"
        
