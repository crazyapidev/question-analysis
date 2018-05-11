from elastic_search_db.es_fetch import FetchFromES
from intents.read_out import ReadOut
from utils.miscellaneous import file_structure
from utils.miscellaneous import fetch_section_with_sub_section_name
# from utils.context_manager import ContextManager

class OperationsException(Exception):
    def __init__(self, foo):
        self.param = foo
        
class Operations(object):
    
    def __init__(self,params,context):
        self.params = params 
        self.context = context
        fetch_content = FetchFromES()
        self.results = fetch_content.fetch_lesson_content_from_es("What's the Weather like")
    
    def get_jsonData(self):
#         file1 = "intro_and_lesson.json"
#         json_data = open (file1).read ()
#         jsonData = json.loads(json_data)
        jsonData = self.results["hits"]["hits"][0]["_source"]
        return jsonData
    
    def get_lessonData(self):
#         file2 = "section_structure.json"
#         lesson_data = open (file2).read ()
#         lessonData = json.loads(lesson_data)
        lessonData = file_structure
        return lessonData
   
    
    def get_segment(self): 
        jsonData = self.get_jsonData()
        
        if self.context["parameters"]["intent"] == "smartlearning.readout.lessonSegment":
            segment = "introduction"
        else :
            segment = "lessons"
        
        for i in range(len(jsonData["books"][0]["segments"])):        
            if jsonData["books"][0]["segments"][i].keys()[0].lower().strip() == segment.lower().strip():
                if i==len(jsonData["books"][0]["segments"])-1:
                    PREVIOUS_SEGMENT = jsonData["books"][0]["segments"][i-1].keys()
                elif i==0:
                    NEXT_SEGMENT = jsonData["books"][0]["segments"][i+1].keys()
                else:
                    PREVIOUS_SEGMENT = jsonData["books"][0]["segments"][i-1].keys()
                    NEXT_SEGMENT = jsonData["books"][0]["segments"][i+1].keys() 
        return PREVIOUS_SEGMENT, NEXT_SEGMENT   
        
    
    def get_lesson_section(self):
        lessonData = self.get_lessonData()
        lesson_section = self.context["parameters"]["lesson_section"]
        sections = lessonData["segments"][0]["lessons"][0]["sections"]
        PREVIOUS_SECTION = ""
        NEXT_SECTION = ""
        for index,section in enumerate(sections):
            if section["section_name"].lower().strip() == lesson_section.lower().strip():
                if index == len(sections)-1 :
                    PREVIOUS_SECTION = sections[index-1]["section_name"]
                elif index == 0 :
                    NEXT_SECTION = sections[index+1]["section_name"] 
                else:
                    PREVIOUS_SECTION = sections[index-1]["section_name"]
                    NEXT_SECTION = sections[index+1]["section_name"]
                    
        return NEXT_SECTION, PREVIOUS_SECTION 
        
    def get_lesson_additional_section(self):
        lessonData = self.get_lessonData()
        lesson_additional_section = self.context["parameters"]["lesson_additional_section"]
        additional_sections = lessonData["segments"][0]["lessons"][0]["additional_sections"]
        PREVIOUS_SECTION = ""
        NEXT_SECTION = ""
        for index,additional_section in enumerate(additional_sections):
            if additional_section["section_name"].lower().strip() == lesson_additional_section.lower().strip():
                if index == len(additional_sections)-1 :
                    PREVIOUS_SECTION = additional_sections[index-1]["section_name"]
                elif index == 0 :
                    NEXT_SECTION = additional_sections[index+1]["section_name"]
                else:
                    PREVIOUS_SECTION = additional_sections[index-1]["section_name"]
                    NEXT_SECTION = additional_sections[index+1]["section_name"]                   
                
        return NEXT_SECTION, PREVIOUS_SECTION
            
            
    def get_introductory_section(self):
        lessonData = self.get_lessonData()
        introductory_section = self.context["parameters"]["introductorySection"]
        sections = lessonData["segments"][1]["introduction"]["sections"]
        PREVIOUS_SECTION = ""
        NEXT_SECTION = ""
        for index,section in enumerate(sections):
            if section["section_name"].lower().strip() == introductory_section.lower().strip():
                if index == len(sections)-1 :
                    PREVIOUS_SECTION = sections[index-1]["section_name"]
                elif index == 0 :
                    NEXT_SECTION = sections[index+1]["section_name"]
                else:
                    PREVIOUS_SECTION = sections[index-1]["section_name"]
                    NEXT_SECTION = sections[index+1]["section_name"]
               
        return NEXT_SECTION, PREVIOUS_SECTION
        
    def get_sub_section(self,lesson_section,lesson_sub_section):
        lesson_data = self.get_lessonData()
        sections = lesson_data["segments"][0]["lessons"][0]["sections"]
        NEXT_SUB_SECTION = ""
        PREVIOUS_SUB_SECTION = ""
        for section in sections:
            if section["section_name"].lower().strip() == lesson_section.lower().strip():
                for index,sub_section in enumerate(section["sub_sections"]):
                    if sub_section["sub_section_name"].lower().strip() == lesson_sub_section.lower().strip():           
                        if index == len(section["sub_sections"])-1:
                            PREVIOUS_SUB_SECTION = section["sub_sections"][index-1]["sub_section_name"]
                        elif index == 0:
                            NEXT_SUB_SECTION = section["sub_sections"][index+1]["sub_section_name"]
                        else:
                            PREVIOUS_SUB_SECTION = section["sub_sections"][index-1]["sub_section_name"]
                            NEXT_SUB_SECTION = section["sub_sections"][index+1]["sub_section_name"]
        
        return NEXT_SUB_SECTION, PREVIOUS_SUB_SECTION 
    
    def repeat_operation(self):
        return self.context["parameters"]["previous_response"] 
    
    def next_segment(self):        
        """
             next section and skip this section 
             treating both these operations as same
        As of now dealing with only introduction segment
        """
        read_out = ReadOut()

        NextSegment, PreviousSegment = self.get_segment() 
        if not NextSegment:
            raise( OperationsException("There is no segment after this."))
        response = "The next segment is " + "<break time='0.5s' />"
        response += read_out.read_segment(NextSegment)
        return response # self.params #Parameters(**self.params)
        
    def previous_segment(self):
        read_out = ReadOut()
        """
        As of now dealing with only introduction segment
        """
        NextSegment, PreviousSegment = self.get_segment()
        
        if not PreviousSegment:
            raise (OperationsException("There are no segment before this"))
        
        response = "The previous segment is " + "<break time='0.5s' />"
        response += read_out.read_segment(PreviousSegment)# self.params #Parameters(**self.params)
        return response 
        
    def next_lesson_section(self):        
        """
             next section and skip this section 
             treating both these operations as same
        As of now we have only one lesson
        """
        read_out = ReadOut()
        
        segment = "lessons"    
        lesson = "What's the weather like"    
        NextSection, PreviousSection = self.get_lesson_section()
        if not NextSection:
            raise(OperationsException("There are no sections after this."))
        self.params["lesson_section"] = NextSection
        attr = "sections"
        
        response = "The next section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,lesson,attr,NextSection) 
        return response 
    
    def previous_lesson_section(self):
        read_out = ReadOut()

        segment = "lessons" 
        lesson = "What's the weather like" 
        NextSection, PreviousSection = self.get_lesson_section()
        if not PreviousSection:
            raise(OperationsException("There are no sections before this."))
        self.params["lesson_section"] = PreviousSection
        attr = "sections"
        
        response = "The previous section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,lesson,attr,PreviousSection) 
        return response 
    
    def next_lesson_additional_section(self):
        """
        As of now we have only one lesson
        """
        read_out = ReadOut()
        
        segment = "lessons"  
        lesson = "What's the weather like"        
        attr = "additional_sections"
        NextSection, PreviousSection = self.get_lesson_additional_section()
        
        if not NextSection:
            raise(OperationsException("There are no sections after this."))
        self.params["lesson_additional_section"] = NextSection
        response = "The next section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,lesson,attr,NextSection)
        return response 
    
    def previous_lesson_additional_section(self):
        """
        As of now we have only one lesson
        """
        read_out = ReadOut()
        
        segment = "lessons"   
        lesson = "What's the weather like"     
        attr = "additional_sections"
        NextSection, PreviousSection = self.get_lesson_additional_section()
        
        if not PreviousSection:
            raise( OperationsException("There are no sections before this."))
        self.params["lesson_additional_section"] = PreviousSection
        response = "The previous section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,lesson,attr,PreviousSection)
        return response 
    
    def next_introductory_section(self):
        read_out = ReadOut()
        
        segment = "introduction"
        NextSection, PreviousSection = self.get_introductory_section()
        attr = "sections"       
        
        if not NextSection:
            raise (OperationsException("There are no sections after this."))
        self.params["introductorySection"] = NextSection
        
        response = "The next section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,"", attr, NextSection)
        return response 
    
    def previous_introductory_section(self):
        read_out = ReadOut()
        
        segment = "introduction"
        attr = "sections"       
        NextSection, PreviousSection = self.get_introductory_section()
        self.params["introductorySection"] = PreviousSection
        if not PreviousSection:
            raise (OperationsException("There are no sections before this."))
        
        response = "The previous section is " + "<break time='0.5s' />"
        response += read_out.read_section(segment,"", attr, PreviousSection)
        return response 
    
    def next_sub_section(self):        
        """
             next section and skip this section 
             treating both these operations as same
        """
        """
        As of now we have only one lesson
        """
        read_out = ReadOut()
       
        segment = "lessons"
        lesson = "What's the Weather Like"
        sub_section =  self.context["parameters"]["lesson_sub_section"] 
        
        try :
            section =  self.context["parameters"]["lesson_section"] 
        except:
            section = fetch_section_with_sub_section_name(sub_section)
            
        """
        TO-DO :: get section name by getting sub_section
        """
        NextSubSection, PreviousSubSection = self.get_sub_section(section,sub_section)
        
        if not NextSubSection:
            raise (OperationsException("There are no sub-sections after this."))
        self.params["lesson_sub_section"] = NextSubSection
        
        
            
        response = "The next sub-section is " + "<break time='0.5s' />"
        response += read_out.read_sub_section(lesson,section,NextSubSection) 
        return response 
        
    def previous_sub_section(self):
        read_out = ReadOut()
       
        segment = "lessons"
        lesson = "What's the Weather Like"
        sub_section =  self.context["parameters"]["lesson_sub_section"] 
        
        try :
            section =  self.context["parameters"]["lesson_section"] 
        except:
            section = fetch_section_with_sub_section_name(sub_section)
            
        """
        TO-DO :: get section name by getting sub_section
        """
        NextSubSection, PreviousSubSection = self.get_sub_section(section,sub_section)
        
        if not PreviousSubSection:
            raise (OperationsException("There are no sub-sections before this."))
        self.params["lesson_sub_section"] = PreviousSubSection
        
        
            
        response = "The previous sub-section is " + "<break time='0.5s' />"
        response += read_out.read_sub_section(lesson,section,PreviousSubSection) 
        return response 
        
    
    def process(self):
        
        operation = self.params["operations"]
        for cntxt in self.context:
            if cntxt["name"] == "operations-followup":
                prev_intent = cntxt["parameters"]["intent"]
                prev_action = cntxt["parameters"]["action"]
                self.context = cntxt
                break
#         pres_intent = self.params["intent"]
        method = operation+"_"+ prev_action
        self.params["intent"] = prev_intent
        self.params["action"] = prev_action
         
        switcher_method = {
            "next_read.segment.introduction" : self.next_segment,
            "previous_read.segment.introduction" : self.previous_segment,
            "next_read.segment.section.content" : self.next_introductory_section,
            "previous_read.segment.section.content" : self.previous_introductory_section,
            "next_.read.segment.lesson" : self.next_segment,
            "previous_read.segment.lesson" : self.previous_segment,
            "next_read.lesson.additionalsection.content" : self.next_lesson_additional_section,
            "previous_read.lesson.additionalsection.content" : self.previous_lesson_additional_section,
            "next_read.lesson.section.content" : self.next_lesson_section,
            "previous_read.lesson.section.content" : self.previous_lesson_section,
            "next_read.lesson.section.subsection.content" : self.next_sub_section,
            "previous_read.lesson.section.subsection.content" : self.previous_sub_section,
            "repeat" : self.repeat_operation
                }
        
        try:
            return switcher_method[method](),self.params
        except KeyError :
            return switcher_method[operation](),self.params       
        except OperationsException as e:
            return e.param,None
        except :           
            return "Not a valid Operation",None
        
        
