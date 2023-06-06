# Python-Google-Cloud-Vision
Python for Google Cloud Vision OCR for Image Folder Organizer

<h3>Before Start</h3>

<ol>
  <li>Setting Up Google Cloud: https://cloud.google.com/vision/docs/setup </li>
  <li>Setting Up Google Cloud Vision API: https://cloud.google.com/vision/docs/labels </li>
  <li>Setting Up sklearn: https://scikit-learn.org/stable/install.html</li>
  <li>Setting Up PyDictionary: https://pypi.org/project/PyDictionary/</li>
  <li>Setting Up nltk (For Lemmatization): https://www.nltk.org/</li>
</ol>


<h3>Entity Annotation Image Response JSON</h3>

This is the response JSON after sending request to Google cloud for labeling the picture.
It seems to have problem with the score and topicality (having same value). (https://issuetracker.google.com/issues/117855698?pli=1)

```
{
  "responses": [
    {
      "labelAnnotations": [
        {
          "mid": "/m/0199g",
          "description": "Bicycle",
          "score": 0.96705616,
          "topicality": 0.96705616
        },
        {
          "mid": "/m/0h9mv",
          "description": "Tire",
          "score": 0.9641615,
          "topicality": 0.9641615
        }
      ]
    }
  ]
}
```
<h3>Folders under Resources</h3>

  <ul>
  <li><b>tmp</b>: Folder that contains the pictures before clustering</li>
  <li><b>results</b>: Folder that contains the pictures of result</li>
  <li><b>pictures</b>: Folder that contains the pictures after clustering</li>
  <li><b>csv</b>: Folder that contains the csv files of dataframe used in the project</li>
  </ul>

<h3>Files</h3>
  
  <ul>
    <li><b>FolderCreater.py</b>: Creating the folder with appropriate cluster and move the image according to the cluster result</li>
    <li><b>KMeanClustering.py</b>: Using the Sklearn Kmean clustering library, it creates the 5 cluster of images. </li>
    <li><b>Lemmatization.py</b>: Using the nltk WorkNetLemmatizer, it preprocesses (lemmatize) the word. (eg. computer, computing, computerize -> compute)</li>
    <li><b>Main.py</b>: Create the dataframe using the labels from the Google Vision API</li>
    <li><b>OCR.py</b>: Opens up the connection with Google Cloud and process Google Vision API labeling</li>
  </ul>
  
<h4> How It Works </h4>

In this project, I mainly used the Google Cloud Vision API to extract the labels of each pictures. The response JSON format is describe above and more detail can be found in https://cloud.google.com/vision/docs/reference/rest/v1/AnnotateImageResponse#EntityAnnotation. 

Then, I mainly used 
```py
label.describe
```
```py
label.topicality
```
to get the appropriate label information and topicality score of the label to the picture. Due to timing issue, I only used top 3 topicaity scored labels when creating dataframe (more in issues).

Using the labels from the Google Vision API, I used PyDictionary which is python library that provides the definition of the word to create the information document of the image.

Using the definition document, I proecess the TF-IDF and lemmatization to creat vector score of each image. Then, using the vector score, I process K mean alogrithm to create the clusters of images.

Information about <b>PyDictionary</b> can be found in: https://pypi.org/project/PyDictionary/

Information about <b>nltk lemmatization</b> can be found in: https://www.nltk.org/_modules/nltk/stem/wordnet.html

Information about <b>kmean sklearn</b> can be found in: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

Information about <b>tfidf skelarn</b> can be found in: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

The result dataframe before clustering:

![df](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/78107826-9331-47ae-8caf-1820e0a8904f)

The result dataframe after clustering:

![df_result](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/2bba277e-6894-4108-9bdc-4cccbf8f2b21)

You can find the csv file under resources/csv

<h3>Result</h3>

<h4>Before Clustering:</h4>

![Before_Sort](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/5cd6602f-320a-454f-827b-878e2363ba92)

<h4>After Clustering:</h4>

![Result_1](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/7424f1b4-2487-4cfc-83a5-ca940294d062)

![Result_2](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/c459318d-6142-4c69-9344-505eea0433e0)

![Result_3](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/16b1007b-bba5-4a0e-b2f4-5f8a8e717b56)

![Result_4](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/1a9e2b1c-65b6-4e16-b8cf-11bcd00b13e2)

![Result_5](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/8fb83fd1-155a-4595-af3f-519bb1228a07)

![Result_6](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/e30f5cc1-7805-4d05-856d-0515c9e3a460)

<h4>Code Proecssing Time:</h4>
![Time](https://github.com/jhkwag970/Python-OCR-Picture-Organizer/assets/54969114/c62a3e20-b6bf-4825-986d-4afa89a9234b)

<h3>Issues & Future Development Plan</h3>

Right now, the name of the folders where label with cluster number. In future, I will try to extact the main concept words from the cluster and use it as the name of the folder.

Issue that the project currently has is the timing issue. Eventhough the code proecess time is relatively low, (~2 total secs), the amount of time for result is about 3-5minutes for 12 pictures. So, the time for clustering will increase when the number of picture also increase

Another issue is Google Clound Vision API that I am using is free trial version. It mean, I cannot use the project after August. Moroever, since it is free trial version, there is limited number of picture that we can process to get labeling. Pricing can be found in (https://cloud.google.com/vision/pricing).

<h4>Credential</h4>

<ul>
  <li> Document Clustering using Sklearn: https://romg2.github.io/mlguide/03_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%99%84%EB%B2%BD%EA%B0%80%EC%9D%B4%EB%93%9C-08.-%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%B6%84%EC%84%9D-%EB%AC%B8%EC%84%9C-%EA%B5%B0%EC%A7%91%ED%99%94/ </li>
  <li>Lemmatization: https://en.wikipedia.org/wiki/Lemmatisation</li>
  <li>TF-IDF Example: https://en.wikipedia.org/wiki/Tf%E2%80%93idf</li>
</ul>
