
import json
import logging
import application_logger
logger = logging.getLogger(__name__)
import os

with open('data/section_structure.json','r') as file:
    file_structure = json.loads(file.read())
        
def fetch_section_with_sub_section_name(sub_section_name):
    sections = file_structure["segments"][0]["lessons"][0]["sections"]
    for section in sections:
        for sub_section in section["sub_sections"]:
            if sub_section["sub_section_name"].strip().lower() == sub_section_name.strip().lower():
                return section["section_name"]
    
def fetch_ordinal_of_section(segment,section_name,attr):
    """
    attr :: sections/sub_sections/additional_sections
    """
    section_content = {
        "introduction_sections" : file_structure["segments"][1]["introduction"]["sections"],
        "lessons_additional_sections" : file_structure["segments"][0]["lessons"][0]["additional_sections"],
        "lessons_sections" : file_structure["segments"][0]["lessons"][0]["sections"]
        }
    
    try :
        sections = section_content[segment +"_"+ attr]
    except KeyError :
        sub_section_name = section_name
        section_name = fetch_section_with_sub_section_name(sub_section_name)
        sections = file_structure["segments"][0]["lessons"][0]["sections"]
        for section in sections:
            if section["section_name"].strip().lower() == section_name.strip().lower():
                sections = section["sub_sections"]
                section_name = sub_section_name
                break
            
    for section_number,section in enumerate(sections):
        if list(section.values())[0].strip().lower() == section_name.strip().lower():
            if section_number == 0:
                return "This is First section"
            elif section_number == len(sections)-1:
                return "This is Last section"
            else:
                return ""
            
"""
Below contexts are for assesment 
context contains present question,total no of questions,previous question
"""
def get_assesment_context(filename):
        with open(filename,"r") as f:
            context = json.load(f)
        return context

def save_assesment_context(context,filename):
    with open(filename, 'w') as outfile:
        json.dump(context, outfile)  
        
def get_user_context_file(params):
    
    user_id=" "
    if params["user_id"]:        
        user_id=  params["user_id"]
        logger.info("assistant id : %s",user_id)                   
    else:
        user_id=  params["sessionId"]
        logger.info("dialogflow id : %s",user_id)
        
    filename = "users/"+user_id+".json"
    
    return filename
    

def update_user_session(params):      
       
    filename = get_user_context_file(params)         
    if not os.path.exists(filename):
        user_session ={
        "status": {
            "present_question": 0,
            "previous_question": 0,
            "staroverprompt": False,
            "total_questions": 0
         },
        "lesson": "What's Weather like",
        "session": "end",
        "type_": "take_quiz",
        "section": ""
        } 
        save_assesment_context(user_session, filename)

