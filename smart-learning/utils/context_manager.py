
import json 
from utils.miscellaneous import get_assesment_context,get_user_context_file,save_assesment_context

class ContextManager():
    
    def __init__(self,context):
        self.context = context
    
    def fetch_data_from_context(self,req_param):
        return self.context[0]["parameters"][req_param]
        
    def set_context_for_read_out(self,params,response):
        cntxt_found = False
        for i,cntxt in enumerate(self.context):
            if cntxt["name"] == "operations-followup":
                cntxt_found = True
                break
        if cntxt_found:
            self.context.pop(i)
        context = {}
        response = response.replace("The next section is ","")
        response = response.replace("The next segment is ","")
        response = response.replace("The previous section is ","")
        response = response.replace("The previous segment is ","")
        
        context["name"] = "operations-followup"
        context["parameters"] = params
        context["parameters"]["previous_response"] = response
        context["lifespan"] = 1
        self.context.insert(0,context)
        return self.context
        
    def set_context_for_assessment(self,params):
        filename=get_user_context_file(params)
        context = get_assesment_context(filename)
        if(context["status"]["total_questions"]!=0):
            if context["status"]["present_question"]==context["status"]["total_questions"]:
                for ctx in self.context:
                    if ctx['name'] == 'smartlearningassessment-followup' or ctx['name'] == 'smartlearningassessment-followup-2':
                        ctx['lifespan'] = 0
        
        return self.context
     
    def set_context_for_assessment_exit(self,params):
        filename=get_user_context_file(params)
        context = get_assesment_context(filename)
        if context["status"]["staroverprompt"]==True:
            context["status"]["staroverprompt"]=False
        save_assesment_context(context,filename)
        for ctx in self.context:
            if ctx['name'] == 'smartlearningassessment-followup' or ctx['name'] == 'smartlearningassessment-followup-2':
                ctx['lifespan'] = 0        
        return self.context
        
        
