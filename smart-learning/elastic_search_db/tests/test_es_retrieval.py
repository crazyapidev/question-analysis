
try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase
from elastic_search_db.es_fetch import FetchFromES

class TestESRetrieval(TestCase):
    
    def test_es_connection(self):
        es_db = FetchFromES()
        es_db.check_es_connection()
    
    def test_es_index_exists(self):
        es_db = FetchFromES()
        es_db.check_index_exists()
        
    def test_es_fetch_content(self):
        es_db = FetchFromES()
        results = es_db.fetch_lesson_content_from_es("What's the Weather Like")
        self.assertIsNotNone(results)
        
    def test_fetch_assessment_qna(self):
        fetch_qna = FetchFromES()
        lesson_name = "What's the weather like"
        results = fetch_qna.fetch_assessment_qna_from_es(lesson_name)
        print (results)
        
    def test_fetch_documents_for_qna_processor(self):
        fetch_qna = FetchFromES()
        query = "seasons year"
        results = fetch_qna.fetch_document_from_es(query)
        print (results)