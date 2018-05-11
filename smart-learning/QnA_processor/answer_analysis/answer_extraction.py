'''
Created on Mar 13, 2018

@author: 574965
'''
from QnA_processor.annotators.datatypes import Document
from QnA_processor.annotators.pipeline import AnnotatorPipeline
from QnA_processor.annotators.sentencer import SentenceAnnotator
from QnA_processor.annotators.tokenizer import TokenAnnotator
from QnA_processor.annotators.word import WordAnnotator
from QnA_processor.annotators.entity_tagger import EntityTagger
from QnA_processor.answer_analysis.simple_sentence_extraction import extract_simple_sentences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class AnswerExtraction():
    
    def __init__(self,query,answer_type,extracted_sentence_object):
        self.query = query
        self.answer_type = answer_type
        self.extracted_sentence_object = extracted_sentence_object
        self.simple_sentences = []
        
    def count_no_of_occurrence_of_answer_type_in_sentence(self,sentence_object):
        count = 0
        for entity in sentence_object.entities:
            if entity.entity_type in self.answer_type:
                count+=1
        return count
    
    def answer_type_entity_present_in_query(self):
        for entity in self.query.entities:
            if entity.entity_type in self.answer_type:
                return True
        return False
        
    def extract_answer(self):
        count = self.count_no_of_occurrence_of_answer_type_in_sentence(self.extracted_sentence_object)
        answer = self.extract_answer_for_single_or_two_entities(count,self.extracted_sentence_object)
        if answer:
            return answer
        else:
            simple_sentence_object_list = []
            count = 0
            self.simple_sentences = extract_simple_sentences(self.extracted_sentence_object.raw_text)
            pipeline=AnnotatorPipeline([TokenAnnotator(),WordAnnotator(),EntityTagger()]) # ,TokenAnnotator(),WordAnnotator()
            for simple_sentence in self.simple_sentences:
                simple_sentence_object = Document(id="sample",text=simple_sentence,raw_text=simple_sentence)
                pipeline.process(simple_sentence_object)
                count = self.count_no_of_occurrence_of_answer_type_in_sentence(simple_sentence_object)
                
                if count>0:
                    simple_sentence_object_list.append((simple_sentence_object,count,self.similarity_measure(self.query.raw_text, simple_sentence)))
                    
            if not simple_sentence_object_list:
                return self.extracted_sentence_object.raw_text
            final_simple_sentence_object = max(simple_sentence_object_list,key=lambda item:item[2])[0]
            count = max(simple_sentence_object_list,key=lambda item:item[2])[1]
            answer = self.extract_answer_for_single_or_two_entities(count,final_simple_sentence_object)
            if answer:
                return answer
            elif count > 0 and not answer:
                return final_simple_sentence_object.raw_text
            else:
                return None
    
    def extract_answer_for_single_or_two_entities(self,count,sentence_object):
        
        if count == 1:
            for entity in sentence_object.entities:
                if entity.entity_type in self.answer_type:
                    return entity.words
        elif count == 2 and self.answer_type_entity_present_in_query():
            for entity in sentence_object.entities:
                if entity.entity_type in self.answer_type:
                    if entity.words.lower() not in self.query.text.lower():
                        return entity.words
              
    def similarity_measure(self,query,passage):
        
        """
        cosine similarity
        """
        tfidf_vectorizer=TfidfVectorizer()
        documents=(query.lower(),passage.lower())
        tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
        cs=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)
        return  cs[0][1]  