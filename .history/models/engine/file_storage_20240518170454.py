
''' 
    FileStorage  class
'''
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
        for key, value in FileStorage.__objects.items():
            dict_object[key] = val.to



