
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
    

    def new(self, obj):
        key = str(obj)

