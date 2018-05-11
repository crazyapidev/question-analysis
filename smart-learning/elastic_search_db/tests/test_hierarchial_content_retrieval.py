try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase
from elastic_search_db.es_fetch import FetchFromES
from elastic_search_db.es_parse_results import ParseESResults

class TestParseESResultsForReadAloud(TestCase):
    
    def test_parsing_introduction_segment(self):
        segment = "introduction"
        section = ""
        sub_section = ""
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's the Weather like")
        parse_content = ParseESResults(results,segment)
        segment_content = parse_content.parse_segment_content()
        self.assertIsNotNone(segment_content)
        
    def test_parsing_lesson_segment(self):
        segment = "lessons"
        lesson = "What's the weather like"
        section = ""
        sub_section = ""
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's the Weather like")
        parse_content = ParseESResults(results,segment,lesson)
        segment_content = parse_content.parse_lesson_content()
        self.assertIsNotNone(segment_content)
        
    def test_parsing_introduction_segment_and_section(self):
        segment = "introduction"
        lesson = "What's the weather like"
        section = "Recommended resources"
        sub_section = ""
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's Weather like")
        parse_content = ParseESResults(results,segment,lesson,section)
        section_content = parse_content.parse_section_content("sections")
        self.assertIsNotNone(section_content)
        
    def test_parsing_lesson_segment_and_section(self):
        segment = "lessons"
        lesson = "What's the weather like"
        section = "Introducing the Read Aloud"
        sub_section = ""
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's Weather like")
        parse_content = ParseESResults(results,segment,lesson,section)
        section_content = parse_content.parse_section_content("sections")
        self.assertIsNotNone(section_content)
        
    def test_parsing_lesson_segment_and_additional_section(self):
        segment = "lessons"
        lesson = "What's the weather like"
        section = "PRIMARY FOCUS OF LESSON"
        sub_section = ""
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's Weather like")
        parse_content = ParseESResults(results,segment,lesson,section)
        section_content = parse_content.parse_section_content("additional_sections")
        self.assertIsNotNone(section_content)
        
    def test_parsing_lesson_segment_and_section_and_sub_section(self):
        segment = "lessons"
        lesson = "What's the weather like"
        section = "Read Aloud"
        sub_section = "Purpose for Listening"
        fetch_content = FetchFromES()
        results = fetch_content.fetch_lesson_content_from_es("What's Weather like")
        parse_content = ParseESResults(results,segment,lesson,section,sub_section)
        section_content = parse_content.parse_sub_section_content("sections")
        self.assertIsNotNone(section_content)
        