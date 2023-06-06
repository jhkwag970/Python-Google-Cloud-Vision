from OCR import ImageLabel
from PyDictionary import PyDictionary
import glob, os
import sys

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import warnings


def csv_save(df):
    os.chdir('resources/csv/')
    df.to_csv('img_df.csv')

def csv_load():
    return pd.read_csv('resources/csv/img_df.csv')

# path="resources/pictures/"
# fileList = os.listdir(path)

# ocr_inst = ImageLabel()
# #Open up Client 
# ocr_inst.open_client()
# #sys.stdout = open('output.txt', 'w')

# #List of all images with own labels and topicalities
# descriptionList=[]
# dictionary=PyDictionary()
# for file in fileList:
#     labels = ocr_inst.detect_labels(path+file)

#     i=0
#     labelList=[]
#     for label in labels:

#         if ' ' in label.description:
#             continue
        
#         labelDefinitions = dictionary.meaning(label.description).get('Noun')

#         if(labelDefinitions == None):
#             labelDefinitions.append(label.description)

#         labelList.append('.'.join(labelDefinitions))
#         i+=1
#         if(i==3):
#             break
    
#     descriptionList.append('. '.join(labelList))


# document_df = pd.DataFrame({'imagename':fileList, 'description':descriptionList})
# csv_save(document_df)

img_df = csv_load()
print(img_df)


