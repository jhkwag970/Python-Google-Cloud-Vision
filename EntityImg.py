class Image:
    def __init__(self, file, annotationList):
        self.__file = file
        self.__annotationList = annotationList
    
    def getFile(self):
        return self.__file
    
    def getAnnotationList(self):
        return self.__annotationList
    
    def toString(self):
        print(self.getFile())
        for k, v in self.__annotationList.items():
            print(k)
            print(v)
        print("-----------------------------------")

