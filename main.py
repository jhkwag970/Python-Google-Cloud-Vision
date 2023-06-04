from OCR import ImageLabel
from EntityImg import Image
from PyDictionary import PyDictionary
import os
import sys

path="resources/"
file_list = os.listdir(path)

ocr_inst = ImageLabel()
#Open up Client 
ocr_inst.open_client()
sys.stdout = open('output.txt', 'w')

# #Label Processing

#List of all images with own labels and topicalities
imgList=[]
dictionary=PyDictionary()
for file in file_list:
    labels = ocr_inst.detect_labels(path+file)

    #list of descriptions and topicalities of one image
    imgDescriptionList={}
    imgTopicalityList=[]
    
    i=0
    for label in labels:
        imgMeaningList=[]

        imgDescriptionList[label]= dictionary.meaning(label)['Noun']
        imgTopicalityList.append(label.topicality)
        #getting only top three (topicalities) labels of image
        i+=1
        if(i==3):
            break
    
    ImgInfo = Image(file, imgDescriptionList, imgTopicalityList)
    imgList.append(ImgInfo)







