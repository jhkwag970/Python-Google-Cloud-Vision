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

csv_path = 'resources/csv/'
def csv_save(df, name):
    os.chdir(csv_path)
    df.to_csv(name, index=False)

def csv_load(name):
    return pd.read_csv(csv_path+name)

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
# csv_save(document_df, 'img_df.csv')

img_df = csv_load('img_df.csv')
print(img_df)

from nltk.stem import WordNetLemmatizer
import nltk
import string

# 단어 원형 추출 함수
lemmar = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmar.lemmatize(token) for token in tokens]

# 특수 문자 사전 생성: {33: None ...}
# ord(): 아스키 코드 생성
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# 특수 문자 제거 및 단어 원형 추출
def LemNormalize(text):
    # 텍스트 소문자 변경 후 특수 문자 제거
    text_new = text.lower().translate(remove_punct_dict)
    
    # 단어 토큰화
    word_tokens = nltk.word_tokenize(text_new)
    
    # 단어 원형 추출
    return LemTokens(word_tokens)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vect = TfidfVectorizer(stop_words='english' , ngram_range=(1,2), 
                             tokenizer = LemNormalize, min_df=0.05, max_df=0.85)

# 피처 벡터화: TF-IDF
feature_vect = tfidf_vect.fit_transform(img_df['description'])

from sklearn.cluster import KMeans

# KMeans: 5
km_cluster = KMeans(n_clusters=5, max_iter=10000, random_state=0)
km_cluster.fit(feature_vect)

# cluster 및 중심 좌표 정보
cluster_label = km_cluster.labels_
cluster_centers = km_cluster.cluster_centers_

# cluster 라벨 추가
img_df['cluster_label'] = cluster_label

csv_save(img_df, 'img_cluster_df.csv')
print(img_df)

