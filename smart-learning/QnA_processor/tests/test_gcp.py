'''
Created on Apr 27, 2018

@author: 574965
'''
{
  "document":{
      "type":"PLAIN_TEXT",
      "content":"what are the different types of weather"
  },
  "classificationConfig":{
      "model":"question_classification_v2_0"
  }
}

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

client = language.LanguageServiceClient()
text = "what are the different types of weather"
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

classificationConfig = {
      "model":"question_classification_v2_0"
  }

categories = client.classify_text(document,classificationConfig).categories

for category in categories:
    print(u'=' * 20)
    print(u'{:<16}: {}'.format('name', category.name))
    print(u'{:<16}: {}'.format('confidence', category.confidence))


 




'''
Google NL API
'''
# class GoogleNLPLibrary():
#     
#     # def __init__(self):
#         
#     #    "Not Implemented"
#     
#     def tag_by_api_call(self,text):
#         import requests
#         import json   
# 
#         url = "https://language.googleapis.com/v1/documents:analyzeSyntax"
#         querystring = {"key":"AIzaSyDElMxqhv85vE2C3mhWR2i4hLpSWEIGLUo"}
#         proxies = {
#             'http': 'http://574965:Mar27%402018%23@proxy.cognizant.com:6050',
#             'https': 'https://574965:Mar27%402018%23@proxy.cognizant.com:6050',
#                    }
# 
#         payload = {
#               "encodingType": "UTF8",
#               "document": {
#                 "type": "PLAIN_TEXT",
#                 "content": text
#               }
#             }
#         
#         headers = {
#             'content-type': "application/json",
#             'cache-control': "no-cache",
#             'postman-token': "ebfea716-f0ff-1a5d-f304-5b514e4d90b8"
#             }
#         
#         response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring,proxies=proxies)
#         return response.text 
#         
#     def tag_by_google_natural_language_package(self):
#         from google.cloud import language
#         from google.cloud.language import enums
#         from google.cloud.language import types
#          
#     def sentencer(self,text):
#         """ Sentence Segmentation """
#         raise NotImplemented
#     
#     def tokenization(self,text):
#         """ Implement tokenization Logic """
#         raise NotImplemented
#     
#     def tag_pos_and_lemma(self,text):
#         print (self.tag_by_api_call(text))
#     
#     def tag_generic_entities(self,text):
#         raise NotImplemented
#     
# if __name__ == "__main__":
#     nlp_library = GoogleNLPLibrary()
#     text = "Summer is the hottest season"
#     nlp_library.tag_pos_and_lemma(text)