from elastic_search_db.es_fetch import FetchFromES
from elastic_search_db.es_parse_results import ParseESResults
# from utils.miscellaneous import fetch_ordinal_of_section


class ReadOut(object):
    
    def __init__(self):
        fetch_content = FetchFromES()
        self.results = fetch_content.fetch_lesson_content_from_es("What's Weather like")
        
    def read_segment(self,segment):
        """
        Any segment contains sections.App can respond back with 
        1. reading list of sections
        or 
        2. start reading with first section content
        """
        
        parse_content = ParseESResults(self.results,segment)
        segment_content = parse_content.parse_segment_content()
        sections = []
        for section in segment_content["sections"]:
            sections.append(section["section_name"])
        
        response = segment + " segment contains " + str(len(sections)) + " sections, They are " + ", ".join(sections[:-1])+ ' and ' + sections[-1]+ \
                    "<break time='0.5s' />. Which section would you like to hear? You can ask me to repeat, skip or jump to the previous or next section anytime"
        
        return response
    
    def read_lesson(self,lesson):
        parse_content = ParseESResults(self.results,"lessons",lesson)
        lesson_content = parse_content.parse_lesson_content()
        
        if not lesson_content:
            return "I cannot read this lesson yet. Is there another lesson I can read for you? "
            
        sections = []
        for section in lesson_content["sections"]:
            sections.append(section["section_name"])
        
        additional_sections = []
        for additional_section in lesson_content["additional_sections"]:
            additional_sections.append(additional_section["section_name"])           
        response =  "Lesson 1, \"What's the weather like?\", contains " + str(len(sections)) + " sections, They are " + ", ".join(sections[:-1])+ ' and ' + sections[-1] + \
                    ". The lesson also contains some precursor content like <break time='1s' />" +", ".join(additional_sections[:-1])+ ' and '+ additional_sections[-1] + \
                    "<break time = '0.5s' />. You can ask me to repeat, skip or jump to the previous or next section anytime"
        return response
        
    def read_section(self,segment,lesson,attr,section,query=""):
        """
            attr :: sections/additional_sections (only for lessons segment)
        """        
        parse_content = ParseESResults(self.results,segment,lesson,section)
        section_content = parse_content.parse_section_content(attr)
        if section_content==None:
            if query=='':
                query="this"
            return "Oops! There is no section with this title "+query+". Please repeat the section title again."
        # response = fetch_ordinal_of_section(segment,section,attr)
        if segment == "lessons" and attr=="sections":
            sub_sections = []
            for sub_section in section_content["sub_sections"]:
                sub_sections.append(sub_section["sub_section_name"])
            response =  section + " section contains " + str(len(sub_sections)) + " sub-sections.They are -" + ", ".join(sub_sections[:-1])+ ' and '+ sub_sections[-1]+ \
                    "<break time = '0.5s' />. You can ask me to repeat, skip or jump to the previous or next sub-section anytime"
            return response
        else:
            
            return self.change_dict_section_content_to_string_content(section_content,"section")
        
    def read_sub_section(self,lesson,section,sub_section,query=""):
        segment = "lessons"
        attr = "sections" # "additional_sections"
        if section==None:
            if query=='':
                query="this"
            return "Oops! There is no sub-section with this title "+query+". Please repeat the sub-section title again."
            #return "There is no sub-section like "+query+".Please say the sub-section name correctly."
        parse_content = ParseESResults(self.results,segment,lesson,section,sub_section)
        sub_section_content = parse_content.parse_sub_section_content(attr)
        if sub_section_content==None:
            if query=='':
                query="this"
            return "Oops! There is no sub-section with this title "+query+". Please repeat the sub-section title again."
        return self.change_dict_section_content_to_string_content(sub_section_content,"sub_section")
    
    def change_dict_section_content_to_string_content(self,content,attr):
        section_name = attr + "_name"
        section_content = attr + "_content"
        section_text = attr + "_text"
        content_text = ""
        try :
            if content[section_name].lower() not in ["check for understanding","comprehension questions","core vocabulary"]:
                content_text = content[section_name] + "<break time='0.5s' /> " 
                if "section_text" in list(content.keys()):
                    content_text += content[section_text] + "<break time='0.5s' />"
                for item in content[section_content]:
                    if "content_name" in list(item.keys()):
                        content_text += item["content_name"] + "<break time='0.5s' />" + item["content_text"] + "<break time='0.5s' />"
                        if "content_sub_text" in list(item.keys()) and item["content_sub_text"][0]:
                            for sub_item in item["content_sub_text"]:
                                if "text" in list(sub_item.keys()) and "sub_text" in list(sub_item.keys()):
                                    content_text += sub_item["text"] + "<break time='0.5s' />" + sub_item["sub_text"] + "<break time='0.5s' />"
                                elif "text" in list(sub_item.keys()) :
                                    content_text += sub_item["text"] + "<break time='0.5s' />"
                                else:
                                    content_text += sub_item["question"] + "<break time='0.5s' />"       
                return content_text  
                       
            elif content[section_name].lower() == "core vocabulary":
                content_text = content[section_name] + "<break time='0.5s' /> " 
                for item in content[section_content]:
                    content_text = content_text + "word <break time='0.5s' />" + item["word"] + "<break time='0.5s' />" + \
                                        "meaning <break time='0.5s' />" + item["word_meaning"] + "<break time='0.5s' />" + \
                                        "example <break time='0.5s' />" + item["word_example"] + "<break time='0.5s' />" + \
                                        "other variations of this word <break time='0.5s' />" + item["word_variations"] + "<break time='0.5s' />" 
                return content_text
            elif content[section_name].lower() in ["check for understanding","comprehension questions"]:
                content_text = content[section_name] + "<break time='0.5s' /> "
                for item in content[section_content]:
                    if item["answer"]:
                        content_text += item["question"] + "<break time='5s' />" + "answer is " + \
                                        item["answer"] + "<break time='0.5s' />"
                    else:
                        content_text += item["question"].replace("min read.", 'min <sub alias="reed">read</sub>.', 1) + "<break time='5s' />"
                return content_text
            
        except Exception as e:
            return "I'm sorry. I didn't quite grasp what you just said."
            
