'''
Created on Mar 30, 2018

@author: 574965
'''
from QnA_processor.answer_analysis.pre_processor import PreProcess
from QnA_processor.answer_analysis.answer_extraction import AnswerExtraction
from QnA_processor.annotators.pipeline import AnnotatorPipeline
from QnA_processor.annotators.entity_tagger import EntityTagger
from QnA_processor.answer_analysis.utils import get_ner_type_for_answer_type

from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock
    
class TestAnswerExtractor(TestCase):
    
    def construct_document_object(self,query):
        pre_process = PreProcess()
        clean_query = pre_process.remove_stopwords(query)
        document_object = pre_process.pre_process(query)
        return document_object
    
#     def test_answer_extraction_for_single_answer_type_entity_in_extracted_sentence(self):
#         query = "Where did Mandela visit Oliver Tambo"
#         sentence_extracted = 'Mandela visit the exiled Oliver Tambo in London'
#         answer_type = 'LOC:GPE'
#         nlp_lib_answer_type = get_ner_type_for_answer_type[answer_type]
#         query_object = self.construct_document_object(query)
#         sentence_object = self.construct_document_object(sentence_extracted)
#         entity_tagger = AnnotatorPipeline([EntityTagger()])
#         entity_tagger.process(query_object)
#         entity_tagger.process(sentence_object)
#         answer_extractor = AnswerExtraction(query_object,nlp_lib_answer_type,sentence_object)
#         answer = answer_extractor.extract_answer()
#         print (answer)
#         self.assertEqual(answer,'London')
          
#     def test_answer_extraction_for_two_answer_type_entities_in_extracted_sentence_and_one_same_as_in_query(self):
#         query = "Whom did Mandela visit in  london"
#         sentence_extracted = "In January 1962, Mandela traveled abroad illegally to attend a conference of African nationalist leaders in Ethiopia, visit the exiled Oliver Tambo in London and undergo guerilla training in Algeria."
#         answer_type = 'HUM:ind'
#         nlp_lib_answer_type = get_ner_type_for_answer_type[answer_type]
#         query_object = self.construct_document_object(query)
#         sentence_object = self.construct_document_object(sentence_extracted)
#         entity_tagger = AnnotatorPipeline([EntityTagger()])
#         entity_tagger.process(query_object)
#         entity_tagger.process(sentence_object)
#         answer_extractor = AnswerExtraction(query_object,nlp_lib_answer_type,sentence_object)
#         answer = answer_extractor.extract_answer()
#         self.assertEqual(answer,'Oliver Tambo')
#          
    def test_answer_extraction_for_multi_answer_type_entities_in_extracted_sentence_but_not_in_query(self):
        query = "Where did Jack went"
        sentence_extracted = "Jack went to Germany, England and France"
        answer_type = 'LOC:GPE'
        nlp_lib_answer_type = get_ner_type_for_answer_type[answer_type]
        query_object = self.construct_document_object(query)
        sentence_object = self.construct_document_object(sentence_extracted)
        entity_tagger = AnnotatorPipeline([EntityTagger()])
        entity_tagger.process(query_object)
        entity_tagger.process(sentence_object)
        answer_extractor = AnswerExtraction(query_object,nlp_lib_answer_type,sentence_object)
        answer = answer_extractor.extract_answer()
        self.assertEqual(answer,'two')


        
        