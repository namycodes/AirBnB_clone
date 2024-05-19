
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
        key = str(object.__class__.name) + "." + str(obj.id)
        dictionary_value = object
        FileStorage.__objects[]

