'''
Created on Feb 23, 2018

@author: 574965
'''

from QnA_processor.annotators.pipeline import AnnotatorPipeline
from QnA_processor.annotators.datatypes import Document,Answer
from QnA_processor.annotators.sentencer import SentenceAnnotator
from QnA_processor.annotators.tokenizer import TokenAnnotator
from QnA_processor.annotators.word import WordAnnotator
from QnA_processor.annotators.entity_tagger import EntityTagger
from QnA_processor.answer_analysis.sentence_feature_extractor import SentenceFeatureExtractor
     
class SentenceExtraction():
    
    def __init__(self,query,answer_type,passage,raw_passage):
        
        """
        sentences is list of doc objects (treating each sentence as single doc)
        """
        
        self.query = query
        self.answer_type = answer_type
        self.passage = passage 
        self.raw_passage = raw_passage
        self.sentence_documents = []
        self.candidate_answers = []
        
    def split_passage_into_sentences(self):
        
        """
        splitting the passage into sentences and storing them in list of sentences
        
        """
        self.clean_sentences = self.passage.split(".")
        self.raw_sentences = self.raw_passage.split(".")
        
    
    def sentence_entity_tagger(self):
        for i,sentence in enumerate(self.clean_sentences):
            if sentence and self.raw_sentences[i]:
                document = Answer(id=i,text=sentence,raw_text=self.raw_sentences[i],annotatitions=[])
                tagger = AnnotatorPipeline([TokenAnnotator(),WordAnnotator(),EntityTagger()])
                tagger.process(document)
                self.sentence_documents.append(document)

    
    def entity_match(self):
        '''
        Matching answer type for question with entity type present in passage.
        '''
        for sentence_document in self.sentence_documents:
            for entity in sentence_document.entities:
                if entity.entity_type in self.answer_type:
                    self.candidate_answers.append(sentence_document)
                    break
    '''
    Based on maximum features having maximum values
    '''
#     def get_best_sentence_from_candidate_sentences(self): 
#         feature_measure = SentenceFeatureExtractor(self.query,self.candidate_answers)
#         best_keyword_match_document = feature_measure.keyword_match()
#         best_similarity_document = feature_measure.similarity_measure()
#         best_longest_seq_match_document  = feature_measure.longest_sequence_match()
#         
#         from collections import defaultdict
#         sent_freq = defaultdict( int )
#         document_dict = {}
#         for w in [best_keyword_match_document,best_similarity_document,best_longest_seq_match_document]:
#             sent_freq[w.text] += 1
#             document_dict[w.text]=w
#         return document_dict[max(sent_freq, key=sent_freq.get)]

    '''
    Based on a sort in the preference order of features
    '''
    def get_best_sentence_from_candidate_sentences(self): 
        feature_measure = SentenceFeatureExtractor(self.query,self.candidate_answers)
        keyword_match_document = feature_measure.keyword_match()
        similarity_document = feature_measure.similarity_measure()
        longest_seq_match_document  = feature_measure.longest_sequence_match()
        
        candidate_sentences = []
        for i in range(len(keyword_match_document)):
            candidate_sentences.append([keyword_match_document[i][0], keyword_match_document[i][1], similarity_document[i][1], longest_seq_match_document[i][1]])
        
        candidate_sentences.sort(key=lambda x: (x[1],x[2],x[3]),reverse=True)    
        return candidate_sentences[0][0]
    
    
    def process(self):
        self.split_passage_into_sentences()
        self.sentence_entity_tagger()
        self.entity_match()
        return self.get_best_sentence_from_candidate_sentences()
    
                    

