
''' 
    FileStorage  class
'''
class FileStorage:
    __file__path = "file.json"
    __objects= {}

    '
    def all(self):
        # returns the object 
        return self.__objects
    

    def new(self, obj):
