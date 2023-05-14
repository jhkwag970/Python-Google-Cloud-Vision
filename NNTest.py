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
