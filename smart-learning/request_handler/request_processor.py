
from request_handler.response_generator import ResponseGenerator
from bs4 import BeautifulSoup
import re

def process_request(request):
    params = request["result"]["parameters"]
    params["intent"] = request["result"]["metadata"]["intentName"]
    params["action"] = request["result"]["action"]
    params["query"] = request["result"]["resolvedQuery"]
    context = request["result"]["contexts"]
    if "originalRequest" in request:
        if "user" in request["originalRequest"]["data"]:             
            params["user_id"]=  request["originalRequest"]["data"]["user"]["userId"]                      
    else :
        params["user_id"]=[]   
    params["sessionId"]=request["sessionId"]
    params,context = check_quiz_intent(params, context)
    response_generator = ResponseGenerator()
    response,context = response_generator.generate_response(params,context)
    return construct_response(response,context)
   
def check_quiz_intent(params,contexts):
    if contexts:
        assesment_active=[context['name'] for context in contexts if context['name'] == 'smartlearningassessment-followup'or context['name'] == 'smartlearningassessment-followup-2']                                  
        if assesment_active and (assesment_active[0]=="smartlearningassessment-followup" or assesment_active[0]=="smartlearningassessment-followup-2"):
            if not params["intent"]=="smartlearning.assessment - custom" and not params["intent"]=="smartlearning.assessment" and not params["intent"]=="smartlearning.assessment - exit" :            
                params["intent"]="smartlearning.assessment - custom"            
                params["action"]="assessment"
            for cntxt in contexts:
                if cntxt['name'] == 'smartlearningassessment-followup' or cntxt['name'] == 'smartlearningassessment-followup-2':
                    cntxt['lifespan'] = 2
    return params ,contexts
    
def construct_response(response,context):
#     def normalize_response(result):
    displayText = response.encode('utf-8')
    soup = BeautifulSoup(displayText)
    response=response.replace("min read.", 'min <sub alias="reed">read</sub>.', 1)
    if context:
        
        action_response =    {
          "speech": "<speak>"+ str(response.encode('utf-8')) +"</speak>",  
          "displayText": re.sub(r'\s+', ' ', soup.get_text()),
          "data": {
            "google": {
              "expect_user_response": True,
              "is_ssml": True      
            }
          },
          "contextOut" :context                       
        }
        
    else :
        action_response =    {
          "speech": "<speak>"+ str(response.encode('utf-8')) +"</speak>",  
          "displayText": re.sub(r'\s+', ' ', soup.get_text()),
          "data": {
            "google": {
              "expect_user_response": True,
              "is_ssml": True      
            }
          }
          # "contextOut" :context    
          }
    return action_response

