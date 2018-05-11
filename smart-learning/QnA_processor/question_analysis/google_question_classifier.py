'''
Created on May 9, 2018

@author: 574965
'''

"""
Parameters for making post requests to the question classifier model (using google's autoML)
"""

import json
from QnA_processor.question_analysis.settings import HTTP_PROXY,HTTPS_PROXY,QUESTION_CLASSIFIER_URL,GOOGLE_API_KEY
from google.auth.transport import requests
from google.oauth2 import service_account

class GoogleQuestionClassifier():
    
    def classify_by_api_call(self,query):
        
        proxies = {
           'http': HTTP_PROXY,
           'https': HTTPS_PROXY,
                  }
         
        url = QUESTION_CLASSIFIER_URL
         
        headers = {
            'content-type': "application/json",
            'authorization': GOOGLE_API_KEY
                  }
        payload = {
                      "document":{
                          "type":"PLAIN_TEXT",
                          "content":query
                      },
                      "classificationConfig":{
                          "model":"question_classification_v2_0"
                      }
                  }
         
        
        response = requests.request("POST", url, 
                        data=json.dumps(payload), headers=headers, proxies=proxies)
        answer_type = json.loads(response.text)["categories"][0]["name"].replace("_",":")
        return answer_type
        
    def classify_by_package(self,query):
        
        credentials = service_account.Credentials.from_service_account_file(
            "CommsMedia-e6083b82e793.json")
        credentials = credentials.with_scopes(
            ['https://www.googleapis.com/auth/cloud-platform'])
    
        # Create a requests Session object with the credentials.
        session = requests.AuthorizedSession(credentials)
        
        headers = {'content-type': "application/json"}
    
        data = {
              "document":{
                  "type":"PLAIN_TEXT",
                  "content":query
              },
              "classificationConfig":{
                  "model":"question_classification_v2_0"
              }
            }
        
        response = session.request('POST', 
                        'https://language.googleapis.com/v1beta2/documents:classifyText',
                        headers=headers,data=json.dumps(data))
        
        response = response.json()
        return response['categories'][0]['name']


