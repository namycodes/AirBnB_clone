#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime


# base class component
class BaseModel:

    # class constructor/initializer
    def __init__(self, *args, **kwargs):

        if (len(kwargs) == 0):
            self.if = str(uuid4())
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    ''' 
        returns the string representation of the class
    '''
    def __str__(self):
        newId = str(uuid4())
        self.id = newId
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    '''
        assigns the current time to the update.at and returns it 
    '''
    def save(self):
        if self.updated_at:
            self.updated_at = datetime.now()
        return self.updated_at

    ''' 
        returns the dictionary representation of the class 
    '''
    def to_dict(self):
        newDict = {}
        if self.__dict__:
            newDict.update(self.__dict__)
            newDict['__class__'] = self.__class__.__name__
            newDict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            newDict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        else:
            return "Error: Instance has no attributes"
        return newDict
