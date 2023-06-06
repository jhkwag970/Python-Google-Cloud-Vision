from PyDictionary import PyDictionary

dictionary=PyDictionary()

list = ["cat", "Siamese", "Felidae"]
meaningList=[]
for item in list:
    tmp = dictionary.meaning(item).get('Noun')
    meaningList.append(". ".join(tmp))

print(len(meaningList))