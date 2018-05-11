from utils.evaluate import Validate
from utils.miscellaneous import  save_assesment_context,get_assesment_context,get_user_context_file
from elastic_search_db.es_fetch import FetchFromES
class Assesment(object):
    
     
    def take_quiz(self,params):
        lesson = "What's the Weather like"      
        fetch_assessment_qna = FetchFromES()
        quiz_content = fetch_assessment_qna.fetch_assessment_qna_from_es(lesson)
        user_response = params["query"]    
        question = '' 
        validation_result = ''   
        filename=get_user_context_file(params)
        context= get_assesment_context(filename)        
        response=''       
        context["lesson"] = lesson   
        question_number = context["status"]["present_question"]
        context["status"]["total_questions"] = len(quiz_content) 
            
        if params["intent"]=="smartlearning.assessment" and context["status"]["present_question"]>0  and context["status"]["present_question"]!=context["status"]["total_questions"] and context["status"]["staroverprompt"]!=True:              
            response+="Would you like to continue the quiz from where you left last time or start over again?"
            question_number= context["status"]["previous_question"]
            context["status"]["staroverprompt"]=True            
            save_assesment_context(context,filename)  
        elif context["status"]["staroverprompt"]==True:
            if params["query"] =="start over" :
                context["status"]["present_question"]=0
                context["status"]["previous_question"]=0
                question_number = context["status"]["present_question"]
                context = self.update_context(context)                               
            else:
                validation_result+="ok lets continue < break time = '1s' />"
                question_number= context["status"]["previous_question"]
                
                    
            if question_number < context["status"]["total_questions"]:
                question = quiz_content[question_number]["question"]      
            context["status"]["staroverprompt"]=False
            save_assesment_context(context,filename)    
            response = validation_result 
            response = response + (question if question else "quiz completed")           
        else:
            if question_number > 0:
                validation_result += self.validate_response(user_response,context,quiz_content)
            context = self.update_context(context)
        
              
            if question_number < context["status"]["total_questions"]:
                question = quiz_content[question_number]["question"]      
            save_assesment_context(context,filename)    
            response = validation_result 
            response = response + (question if question else "quiz completed")    
        return response
  
    def validate_response(self,user_response,context,quiz_content):
        question_number = context["status"]["previous_question"]
        answer = quiz_content[question_number]["answer"]
        answer_type = quiz_content[question_number]["question_type"]
        result =  Validate().validate(user_response, answer, answer_type)
        result =   result  +"<break time='1s' />\n"
        return result  
      
    def update_context(self,context):
        
        context["type_"] = "take_quiz"
        
        context["status"]["previous_question"] = context["status"]["present_question"]
        
        if context["status"]["present_question"] < context["status"]["total_questions"]:
            context["status"]["present_question"] +=1
            
        if context["status"]["previous_question"] == context["status"]["total_questions"]:
            context["session"] = "end"
            context["status"]["previous_question"] = 0
            context["status"]["present_question"] = 0
            context["status"]["total_questions"] = 0
            context["section"] = ""
        else :
            context["session"] = "continuing"
            
        return context 
            

            
     
