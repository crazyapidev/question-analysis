try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase
from types import ModuleType
from request_handler.response_generator import ResponseGenerator
get_response = ResponseGenerator()

class TestResponseGenerator(TestCase):
    
    def test_read_lesson(self):
        params = {
                  "intent" : "smartlearning.readout.lessonSegment",
                  "action" : "read.lesson.content",
                  "query" : "",
                  "lesson_name" : "What's the weather like"
                }
        context = []
        result,context = get_response.generate_response(params,context)
        expected_result = "Lesson What's the weather like, contains 4 sections, They are Introducing the Read Aloud Read Aloud Application Take Home Material and 5 additional sections, They are PRIMARY FOCUS OF LESSON LESSON AT A GLANCE FORMATIVE ASSESSMENT ADVANCE PREPARATION CORE VOCABULARY"
        self.assertEqual(result,expected_result)
        
    def test_read_segment(self):
        params = {
                  "segment": "introduction",
                  "intent" : "smartlearning.readout.introductorySegment",
                  "action" : "read.segment.introduction",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        expected_result = "introduction segment contains 7 sections, They are Introduction Domain components  Recommended resources WHY SEASONS AND WEATHER ARE IMPORTANT  Core content objectives  Core vocabulary for season & weather  Writing "
        self.assertEqual(result,expected_result)
        
    def test_read_additional_sections(self):
        params = {
                  "lesson_additional_section": "CORE VOCABULARY",
                  "introductorySection": "",
                  "intent" : "smartlearning.readout.lesson.additionalSection",
                  "action": "read.lesson.additionalsection.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        print (result)
        self.assertIsNotNone(result)
        
    def test_read_lesson_sections(self):
        params = {
                  "lesson_section": "Read Aloud",
                  "intent" : "smartlearning.readout.lesson.section",
                  "action": "read.lesson.section.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        expected_result = "Read Aloud section contains 5 sections, They are Purpose for Listening WHAT'S THE WEATHER LIKE Comprehension Questions Word Work Characteristics Check for Understanding"
        self.assertEqual(result,expected_result)
        
    def test_read_lesson_read_aloud_sub_sections(self):
        params = {
                  "lesson_section": "Read Aloud",
                  "lesson_sub_section": "Word Work Characteristics",
                  "intent" : "smartlearning.readout.lesson.subsection",
                  "action": "read.lesson.section.subsection.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        print (result)
        self.assertIsNotNone(result)
        
    def test_read_lesson_application_sub_sections(self):
        params = {
                  "lesson_section": "Application",
                  "lesson_sub_section": "Weather Diary",
                  "intent" : "smartlearning.readout.lesson.subsection",
                  "action": "read.lesson.section.subsection.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        print (result)
        self.assertIsNotNone(result)
        
    def test_read_lesson_introducing_read_aloud_sub_sections(self):
        params = {
                  "lesson_section": "Introducing the Read Aloud",
                  "lesson_sub_section": "Check for understanding",
                  "intent" : "smartlearning.readout.lesson.subsection",
                  "action": "read.lesson.section.subsection.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        print (result)
        self.assertIsNotNone(result)
        
    def test_read_segment_sections(self):
        params = {
                  "segment" : "introduction",
                  "introductorySection": "Domain components",
                  "intent" : "smartlearning.readout.introductorySection",
                  "action": "read.segment.section.content",
                  "query" : ""
                }
        context = []
        result,context = get_response.generate_response(params,context)
        print (result)
        self.assertIsNotNone(result)
        
        