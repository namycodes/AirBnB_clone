
''' 
    FileStorage  class
'''
class FileStorage:
    __file__path = "file.json"
    __objects= {}

    ''' public instance all'''
    def all(self):
        return __objects
    

    def new