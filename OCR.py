from google.cloud import vision
import io
import os

class ImageLabel:

    def open_client(self):
        print("Open up Google Cloud Client Connection...")
        self.__client = vision.ImageAnnotatorClient()
        

    def detect_labels(self,path):
        path = os.path.abspath(path)

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.__client.label_detection(image=image)
        labels = response.label_annotations


        # for label in labels:
        #     print(label.description)

        # if response.error.message:
        #     raise Exception(
        #         '{}\nFor more info on error messages, check: '
        #         'https://cloud.google.com/apis/design/errors'.format(
        #             response.error.message))    
        
        return labels




