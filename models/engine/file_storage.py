"""
    FileStorage  class
"""
import models
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        # returns the object (dictionary)
        return self.__objects

    def new(self, obj):
        if obj:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            value_dict = obj
            FileStorage.__objects[key] = value_dict

        return "object not defined"

    def save(self):
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as data:
                FileStorage.__file_path = json.load(data)

            for key, val in FileStorage.__objects.items():
                class_name = val["__class_name__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)

        except FileNotFoundError:
            pass
