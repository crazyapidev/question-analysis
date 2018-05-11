# -*- coding: utf-8-sig -*-
  
synonyms_dict_lesson_1 = {'different':['various','varied'],'kinds':['forms','types','sorts'],
                         'mostly':['often','usually','generally','commonly','most'],
                         'often':['usually','generally','commonly','most','mostly'],
                         'stand':['mark','denote','depict','represent','show','indicate','point'],'land':['ground'],'ground':['land'],
                         'covered':['full','filled','surrounded','surrounds','abundant','abundance','abound','plenty'],
                         'usually':['often','generally','commonly','mostly'], 
                         'always':['often','generally','commonly','mostly','usually'],
                         'hottest':['warmest'],'hot':['warm'],'warm':['hot'],'located':['situated','present'],
                         'section':['region','area','regions','areas'],'start':['begin','begins'], 
                         'cover':['full','covers','fills','surrounds','covered','filled','surrounded'],'wintertime':['winter','winters'],
                         'begins':['starts','start','begin'],'called':['known as'],'after':['follows','followed','succeeds'],
                         'comes':['occurs','arrives'],'pattern':['characteristic','characteristics'],
                         'easiest':['easy','easily'],'summer':['summers'],'area':['region','section','regions','sections'],
                         'spot':['see','notice','observe']} 

'''
GOOGLE AUTO-ML classifier test
'''

import json
import requests
 
proxies = {
   'http': 'http://574965:Mar27%402018%23@proxy.cognizant.com:6050',
   'https': 'https://574965:Mar27%402018%23@proxy.cognizant.com:6050',
          }
url = "https://language.googleapis.com/v1beta2/documents:classifyText"
 
headers = {
    'content-type': "application/json",
    'authorization': "Bearer ya29.c.Elq3BY-PFCJC4rP1yAg9sCBgMsXYLPm60I4HG_Nbv2-NRQRLm4pHbp70s0nROGHL20T-m8cgAwmVGwvFRkl7-pb67pK0ksWaguoo1_yWv4E7D-D5a_dON3ajqik",
          }
 
payload = {
  "document":{
      "type":"PLAIN_TEXT",
      "content":"Which animal sleeps during winters?"
  },
  "classificationConfig":{
      "model":"question_classification_v2_0"
  }
}
 
response = requests.request("POST", url, data=json.dumps(payload), headers=headers, proxies=proxies)
 
print(response.text)
print(json.loads(response.text)["categories"][0]["name"].replace("_",":"))


'''
Google NLP API entity analyzer test
'''

# import requests
# 
# url = "https://language.googleapis.com/v1/documents:analyzeEntities"
# 
# proxies = {
#    'http': 'http://574965:Mar27%402018%23@proxy.cognizant.com:6050',
#    'https': 'https://574965:Mar27%402018%23@proxy.cognizant.com:6050',
#           }
#  
# querystring = {"key":"AIzaSyDElMxqhv85vE2C3mhWR2i4hLpSWEIGLUo"}
# 
# payload = "{\n  \"encodingType\": \"UTF8\",\n  \"document\": {\n    \"type\": \"PLAIN_TEXT\",\n    \"content\": \"antarctica is in North America and United States is in washington dc\"\n  }\n}"
# headers = {
#     'content-type': "application/json",
#     'cache-control': "no-cache",
#     'postman-token': "9ab8574e-948d-f190-cd67-f62bf8d63938"
#     }
# 
# response = requests.request("POST", url, data=payload, headers=headers, params=querystring,proxies=proxies)
# 
# print(response.text)

'''
FOR SYNONYMS
'''
            
# new_query='' 
# query= 'which areas does the color blue on the map represent'      
# for token in query.split():
#     c=0
#     for key in synonyms_dict_lesson_1.keys():
#         if token in synonyms_dict_lesson_1[key]:
#             if c==0:
#                 new_query = new_query + token + ' ' + key + ' '
#                 c = c+1
#             else:
#                 ew_query = new_query + key + ' '
#     if c==0:
#         new_query = new_query + token + ' '
# 
# print(new_query)

# from fuzzywuzzy import fuzz
# query = 'weather like summer'
# choices = ['I’ve colored two areas map blue', 'color blues often used stand things cold']
# for i in choices:
#     print(fuzz.ratio(query, i))
#     print(fuzz.partial_ratio(query, i))
#     print('**********************************')