from PyDictionary import PyDictionary
dictionary=PyDictionary()

print (dictionary.meaning("cat").get("adj"))

if(dictionary.meaning("cat").get("adj") == None):
    print("this")
