class Image:
    def __init__(self, file, annotationList, topicalityList):
        self.__file = file
        self.__annotationList = annotationList
        self.__topicalityList = topicalityList
    
    def getFile(self):
        return self.__file
    
    def getAnnotationList(self):
        return self.__annotationList
    
    def getTopicalityList(self):
        return self.__topicalityList
    
    def toString(self):
        print(self.getFile())
        for annotation, topicality in zip(self.__annotationList, self.__topicalityList):
            print(annotation, ": ", topicality)
        print("---------------------------------")

