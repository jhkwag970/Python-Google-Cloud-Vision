from OCR import ImageLabel

ocr_inst = ImageLabel()
#Open up Client 
ocr_inst.open_client()
#Label Processing
label = ocr_inst.detect_labels("resources/wakeupcat.jpg")

#Examples
print(label)
print("-----------------------------")
print(type(label))
print("-----------------------------")
print(label[0].description)
print(label[0].score)
print(label[0].topicality)
print("-----------------------------To list ----------------")
label_list=list(label)
print(label_list)
print("-----------------------------")
print(type(label_list))
print("-----------------------------")
print(label_list[0].description)
print(label_list[0].score)
print(label_list[0].topicality)


