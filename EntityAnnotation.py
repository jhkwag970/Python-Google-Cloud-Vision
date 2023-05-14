class Annotation:
    def __init__(self,file,description):
        self.__file = file
        self.__description = description

    def getFile(self):
        return self.__file
    
    def getDesc(self):
        return self.__description
    
    def toString(self):
        print("File: ",self.getFile())
        print("desc: ",self.getDesc())
        print("-------------------------")
