
''' 
    FileStorage  class
'''
class FileStorage:
    __file__path = "file.json"
    __objects= {}

    ''' public instance all'''
    def all(self):
        return self.__objects
    

    def new(self, obj):
