from nltk.stem import WordNetLemmatizer
import nltk
import string
import shutil

# lemmatize the words
lemmar = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmar.lemmatize(token) for token in tokens]

# create ascii code dictionary of special symbols with none value
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# using ascii code dictionary to remove ascii co
def LemNormalize(text):
    text_new = text.lower().translate(remove_punct_dict)
    
    word_tokens = nltk.word_tokenize(text_new)
    
    return LemTokens(word_tokens)