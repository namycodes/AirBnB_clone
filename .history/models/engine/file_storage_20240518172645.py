
''' 
    FileStorage  class
'''
import json


class FileStorage:
    __file__path = "file.json"
    __objects= {}

    '
    def all(self):
        # returns the object (dictionary)
        return self.__objects
    

    def new(self, object):
        if self.__objects:      
            key = str(object.__class__.name) + "." + str(object.id)
            dictionary_value = object
            FileStorage.__objects[key] = dictionary_value

        return ("object not defined")

    def save(self):
        dict_object = {}

        for key, value in self.__objects.items():
            dict_object[key] = value.to_dict()

        with open(self.__file__path, mode="w", encoding="UTF8") as data:
            json.dump(dict_object, data)

    def reload(self):
        try:
            with open(self.__file__path, encoding="UTF8") as data:
                self.__file__path = json.load(data)

            for key, val in self.__objects.items():
                clas
        except
