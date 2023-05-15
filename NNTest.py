def sameWordCluster():
    from EntityAnnotation import Annotation
    anno1 = Annotation("zxc","c")
    anno2 = Annotation("zxc","a")
    anno3 = Annotation("zxc","b")

    list = [anno1, anno2, anno3]

    sortList = sorted(list, key=lambda x:x.getDesc(), reverse=True)

    for ann in sortList:
        ann.toString()

def synCluster():
    import nltk
    nltk.download('wordnet')

    from nltk.corpus import wordnet

    synonyms = []
    for syn in wordnet.synsets("computer"):
        for lm in syn.lemmas():
                 synonyms.append(lm.name())#adding into synonyms
    print (set(synonyms))

    nextSyn = []
    for word in set(synonyms):
           for syn in wordnet.synsets(word):
                  for lm in syn.lemmas():
                         nextSyn.append(lm.name().lower())

    print(set(nextSyn))

def stemmingCluster():
    from nltk.stem import PorterStemmer
    
    ps = PorterStemmer()
    
    # choose some words to be stemmed
    words = ["computer", "computing", "computerize"]
    
    for w in words:
        print(w, " : ", ps.stem(w))


#PyDictionary
#https://pypi.org/project/PyDictionary/
#pip install -e git+https://github.com/yeahwhat-mc/goslate#egg=goslate
#pip install PyDictionary

# from PyDictionary import PyDictionary
# dictionary=PyDictionary()

# print (dictionary.meaning("church"))


# import spacy

# nlp = spacy.load('en') 

# apples, and_, oranges = nlp(u'apples and oranges')
# apples.similarity(oranges)

import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the list of words
words = ['Carnivore', 'cat', 'dog', 'dog breed', 'dog clothes', 'dog supply', 'felidae', 'plant', 'siamese', 'sky', 'temple', 'tower', 'vertebrate', 'world']

# Create a TfidfVectorizer object to convert words to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(words)

# Cluster the vectors using k-means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Print the cluster labels and the words in each cluster
for i in range(kmeans.n_clusters):
    cluster_words = [words[j] for j in range(len(words)) if kmeans.labels_[j] == i]
    print(f"Cluster {i}: {cluster_words}")



