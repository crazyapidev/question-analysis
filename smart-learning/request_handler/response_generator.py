
from intents import miscellaneous 
from intents.read_out import ReadOut
from intents.assesment import Assesment
from intents.operations import Operations
from utils.miscellaneous import fetch_section_with_sub_section_name,update_user_session
from utils.miscellaneous import fetch_ordinal_of_section
from utils.context_manager import ContextManager


class ResponseGenerator():
        
    def miscellaneous(self):
        """
        params = {"miscellaneous" : "(some entity)"}
        get the corresponding field value from dict
        """
        response = miscellaneous.process(self.params) # self.params # Parameters(**self.params)
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def read_segment(self):
        read_out = ReadOut()
        """
        As of now dealing with only introduction segment
        """
        segment = self.params["segment"].lower()
#         self.params["segment"] = segment
        response = read_out.read_segment(segment)# self.params #Parameters(**self.params)
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    
    def read_segment_section(self):
        read_out = ReadOut()
        """
        As of now dealing with only introduction segment,
        TO-DO need to get segment name for a given section name 
            if other segments also implemented
        """
        segment = "introduction" # self.params["segment"].lower()
        section = self.params["introductorySection"]
        """
        attr :: lesson segment have sections & additional sections attibute
                other segments only have sections attribute
        """
        attr = "sections"
#         self.params["segment"] = segment
        # response = fetch_ordinal_of_section("introduction",section, "sections")
        response = read_out.read_section(segment,"",attr,section,self.params["query"])# self.params #Parameters(**self.params)
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def read_lesson_segment(self):
        response = "Which lesson would you like to hear?"
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
        
    def read_lesson(self):
        read_out = ReadOut()
        """
         As of now we are dealing with only one lesson
         "What's weather like"
        """
#         lesson = "What's the Weather Like?"
        lesson = self.params["lesson_name"]
        response = read_out.read_lesson(lesson)
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def read_lesson_section(self):
        read_out = ReadOut()
        """
        As of now we have only one lesson
        """
        segment = "lessons"
        lesson = "What's the Weather Like"
        section = self.params["lesson_section"]
        attr = "sections"
        # response = fetch_ordinal_of_section( "lessons",section, "sections")
        response = read_out.read_section(segment,lesson,attr,section,self.params["query"])
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def read_lesson_additional_section(self):
        read_out = ReadOut()
        """
        As of now we have only one lesson
        """
        segment = "lessons"
        lesson = "What's the Weather Like"
        attr = "additional_sections"
        section = self.params["lesson_additional_section"]
        # response = fetch_ordinal_of_section( "lessons",section, "additional_sections")
        response = read_out.read_section(segment,lesson,attr,section,self.params["query"])
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def read_lesson_sub_section(self):
        read_out = ReadOut()
        context_manager = ContextManager(self.context)
        """
        As of now we have only one lesson
        """
        segment = "lessons"
        lesson = "What's the Weather Like"
        sub_section = self.params["lesson_sub_section"]
        #try :
        #    section = context_manager.fetch_data_from_context("lesson_section")
        #except:
        section = fetch_section_with_sub_section_name(sub_section)

        # response = fetch_ordinal_of_section("lessons",sub_section,  "sub_sections")
        response = read_out.read_sub_section(lesson,section,sub_section,self.params["query"]) 
        self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
    
    def operations(self):
        operations = Operations(self.params,self.context)
        response,self.params  = operations.process()
        if self.params:
            self.context = self.context_manager.set_context_for_read_out(self.params,response)
        return response,self.context
      
    def assesment(self):        
        """
        As of we have only one lesson so directly taking questions 
            of that lesson
        Taking questions from "Check Your Understanding" and "Comprehension" sub_sections
            both are in Read-Aloud section in lesson 
        """
        update_user_session(self.params)
        assesment = Assesment()
        context_manager = ContextManager(self.context)
        if self.params["intent"]=="smartlearning.assessment - exit":
            context = context_manager.set_context_for_assessment_exit(self.params)            
            response="you left the quiz < break time='1s' />you can continue the quiz later."
        else:
            context = context_manager.set_context_for_assessment(self.params)
            response = assesment.take_quiz(self.params)   
        
#         return context_manager.normalize_response_with_context(assesment.take_quiz(self.params["query"],self.params),self.context)
        return response,context
        
        
    def questions(self):
        from QnA_processor.get_answer import get_answer
        query = self.params["query"]
        response = get_answer(query)
        self.context = self.context_manager.set_context_for_read_out(self.params, response)
        return response,self.context
    
        
    def definition(self):
        "Not Implemented"
        
    def generate_response(self,params,context):
        self.params = params
        self.context = context
        self.context_manager = ContextManager(self.context)
        switcher = {
            "assessment" : self.assesment,
            "miscellaneous" : self.miscellaneous,
            "operations" : self.operations,
            "questions" : self.questions,
            "read.segment.introduction" : self.read_segment,
            "read.segment.section.content" : self.read_segment_section,
            "read.segment.lesson" : self.read_lesson_segment,
            "read.lesson.additionalsection.content" : self.read_lesson_additional_section,
            "read.lesson.section.content" : self.read_lesson_section,
            "read.lesson.section.subsection.content" : self.read_lesson_sub_section,
            "smartlearning.vocabDefinition" : self.definition,
            "read.lesson.content" : self.read_lesson
        }
        
        try:
            return switcher[self.params["action"]]()
        except Exception as e:
            print(e)
            return "I'm sorry. I didn't quite grasp what you just said.",self.context

