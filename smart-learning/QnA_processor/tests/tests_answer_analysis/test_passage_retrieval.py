from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.answer_analysis.passage_feature_extractor import PassageFeatureExtractor

class TestPassageFeatureExtractor(TestCase):
    
    def load_document_data(self):
        with open('martin_luther_king.txt','r') as f:
            document = f.read()
        return document
        
    def test_extract_no_of_keyword_feature(self):
        query = "When was King born"
        document = self.load_document_data()
        passage_feature = PassageFeatureExtractor()
        print (passage_feature.no_of_question_keywords_in_passage(query, document))
         
    def test_no_of_right_type_entities(self):
        query = "When was King born"
        entity_type = "DATE"
        document = self.load_document_data()
        passage_feature = PassageFeatureExtractor()
        print (passage_feature.no_of_entities_of_right_type_in_passage(entity_type, document))
         
    def test_longest_sequence(self):
        document = self.load_document_data()
        query = "When was King born"
        passage_feature = PassageFeatureExtractor()
        print (passage_feature.longest_sequence_match_with_query(query, document))
        
    
        