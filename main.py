from OCR import ImageLabel
from PyDictionary import PyDictionary
import os, time
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

csv_path = 'resources/csv/'
path="resources/pictures/"

def csv_save(df, name):
    os.chdir(csv_path)
    df.to_csv(name, index=False)

def csv_load(name):
    return pd.read_csv(csv_path+name)

def creatingDf(ocr_inst, fileList):
    start=time.process_time()
    #List of all images with own labels and topicalities
    descriptionList=[]
    topicalityList=[]
    dictionary=PyDictionary()
    for file in fileList:
        labels = ocr_inst.detect_labels(path+file)

        i=0
        labelList=[]
        for label in labels:

            if ' ' in label.description:
                continue

            if i == 0:
                topicalityList.append(label.description)
            
            labelDefinitions = dictionary.meaning(label.description).get('Noun')

            if(labelDefinitions == None):
                labelDefinitions.append(label.description)

            labelList.append('.'.join(labelDefinitions))

            i+=1
            if(i==3):
                break
        
        descriptionList.append('. '.join(labelList))

    end=time.process_time()
    print("Total Process_time: ", end-start, "seconds")
    return pd.DataFrame({'imagename':fileList, 'description':descriptionList, 'topicality':topicalityList})


totalStart=time.process_time()
fileList = os.listdir(path)

ocr_inst = ImageLabel()
#Open up Client 
ocr_inst.open_client()

img_df = creatingDf(ocr_inst, fileList)

import TfidfVectorizer

feature_vect = TfidfVectorizer.Tfidf(img_df)

import KMeanClustering

KMeanClustering.clustering(feature_vect, img_df)

import FolderCreater

FolderCreater.folderCreate(img_df, path)

totalEnd=time.process_time()

print("Total Process_time: ", totalEnd-totalStart, "seconds")
