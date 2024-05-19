__all__ = ["base_model"]

from .base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

'''
    Working with custom modules
'''

# creating classes
classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

# creating an instance of the File-storage

storage = FileStorage()
storage.reload()
