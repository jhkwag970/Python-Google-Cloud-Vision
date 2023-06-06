
from sklearn.feature_extraction.text import TfidfVectorizer
import Lemmatization, time

def Tfidf(img_df):
    tfidf_vect = TfidfVectorizer(stop_words='english' , ngram_range=(1,2), 
                             tokenizer = Lemmatization.LemNormalize, min_df=0.05, max_df=0.85)
    # TF-IDF
    return tfidf_vect.fit_transform(img_df['description'])
    

