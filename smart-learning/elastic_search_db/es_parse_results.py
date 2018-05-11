
class ParseESResults():
    
    def __init__(self,results,segment=None,lesson=None,section=None,sub_section=None):
        self.results = results
        self.segment = segment 
        self.lesson = lesson
        self.section = section
        self.sub_section = sub_section
        self.parse_book_content()
        
    def parse_book_content(self):
        """
        As of now we have only one book 
          -> "Seasons and Weather Teacher Guide"
        """
        books = self.results["books"]
        for book in books:
            if book["book_name"].lower() == "Seasons and Weather Teacher Guide".lower():
                self.segments = book["segments"]
                
    def parse_segment_content(self):
        for item in self.segments:
            if item.get(self.segment):
                return item[self.segment]
                
            
    def parse_lesson_content(self):
#         lesson = "What's the Weather Like?"
        for item in self.parse_segment_content():
            if item["lesson_name"].strip().lower() == self.lesson.strip().lower():
                return item
        
        
    def parse_section_content(self,attr):
        
        """
        attr :: sections/additional_sections 
        
            introduction only have sections attr 
            whereas lesson have both sections and additional_sections 
            
        So, sectional content can be either sectional or additional sectional content
        depends on the attr (sections/additional_sections)
        """
        
        content = self.parse_segment_content()
        if self.segment.strip().lower() == "lessons":
            content = self.parse_lesson_content()
            
        sections = content[attr]
        for item in sections:
            if item["section_name"].strip().lower() == self.section.strip().lower():
                return item
            
    def parse_sub_section_content(self,attr):
        """
        attr :: sections/additional_sections 
            for retrieving sectional level content
        """
        content = self.parse_section_content(attr)
        
        for item in content["sub_sections"] :
            if item["sub_section_name"].strip().lower() ==self.sub_section.strip().lower():
                return item
            
            
    

