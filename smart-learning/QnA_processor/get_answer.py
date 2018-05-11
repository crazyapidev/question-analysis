# -*- coding: utf-8-sig -*-
"""
Entire Pipeline/Flow to get answer 
"""
from QnA_processor.answer_analysis.pre_processor import PreProcess
from QnA_processor.answer_analysis.passage_extraction import PassageExtraction
from QnA_processor.answer_analysis.sentence_extraction import SentenceExtraction
# from QnA_processor.answer_analysis.answer_extraction import AnswerExtraction
from QnA_processor.answer_analysis.utils import get_ner_type_for_answer_type
from QnA_processor.question_analysis.utils import rephrase_query_with_synonyms
from QnA_processor.question_analysis.question_classifier import classify_question
from elastic_search_db.es_fetch import FetchFromES


"""
MAIN
"""    
def get_answer(query):
    
    """
    Question Ananlyzer 
        1. question classification
        2. rephrasing question with synonyms
    """
    answer_type = classify_question(query)
        
    nlp_lib_answer_type = get_ner_type_for_answer_type[answer_type] 
    
    query = rephrase_query_with_synonyms(query)
    
    """ 
    Loading the PreProcess class to pre-process queries and passages
    Pre Processing query to remove punctuations, stopwords and replace words(verbs) with their lemmatized forms
    """
    pre_process = PreProcess()
    query_object = pre_process.pre_process(query)
#     entity_tagger = AnnotatorPipeline([EntityTagger()])
#     entity_tagger.process(query_object)
    
    '''
    DOC (PASSAGES)-RETRIEVAL FROM ELASTICSEARCH
    '''
    document_fetcher = FetchFromES()
    documents = document_fetcher.fetch_document_from_es(query)
                
    """
    joining all documents to convert into single document seperated by "\n\n" (denotes the start of a new passage) 
     
    """
    merged_document = "\n\n".join(documents)
    passages = merged_document.split("\n\n")
    
    """
    Pre Processing documents to remove punctuations, stopwords and replace words(verbs) with their lemmatized forms
    
    """
    
    passage_objects = []
    for passage in passages:
        passage_object = pre_process.pre_process(passage)
        passage_objects.append(passage_object)
        
        
    """
    CANDIDATE PASSAGES EXTRACTOR
     
    """
    passage_extractor = PassageExtraction(query_object,nlp_lib_answer_type,passage_objects)
    candidate_passages = passage_extractor.process()
    
    """
    Checking for presence of at least one candidate passage
    """
    
    if candidate_passages and candidate_passages[0]:
        
        """
        SENTENCE EXTRACTION 
        
        Considering 1st passage(among candidate passages) as the required passage; using this passage to extract sentence 
        
        Sentence retrieval is on the basis of keyword percent match, similarity score and longest sub-sequence match
        
        Final sentence selected after sorting above features 
        
        """
        sentence_extractor = SentenceExtraction(query_object.text,nlp_lib_answer_type,candidate_passages[0][0].text,candidate_passages[0][0].raw_text)
        final_sentence = sentence_extractor.process()
        return final_sentence.raw_text
        
    else:
        """
        candidate passages have no elements when at least 2 keywords from query are not present in either of the passages 
        """
        return "REPHRASE THE QUESTION"
        
    
#      
#     """
#     ANSWER EXTRACTION
#     """
#       
#     answer_extractor = AnswerExtraction(query_object,nlp_lib_answer_type,final_sentence)
#     print(answer_extractor.extract_answer())

# if __name__== "__main__":
#        
#     data = ['LOC:other-When are the plants full of leaves, flowers and fruits?']
#     for question in data:
#         if question:
#             query = question.split("-")[1].replace('\n','')
#             print(get_answer(query)) 