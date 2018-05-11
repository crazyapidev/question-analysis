
from QnA_processor.answer_analysis.passage_feature_extractor import PassageFeatureExtractor
from QnA_processor.annotators.pipeline import AnnotatorPipeline
from QnA_processor.annotators.entity_tagger import EntityTagger

class PassageExtraction():
    
    def __init__(self,query_object,answer_type,passage_objects):
        self.query_object = query_object
        self.clean_query =  self.query_object.text #clean_query
        self.answer_type = answer_type
        self.passage_objects = passage_objects
        self.feature_vector = []
        self.no_of_entities_of_right_type = 0
        
    
    def no_of_entities_of_right_type_in_passage(self,passage_object):
        for entity in passage_object.entities:
            if entity.entity_type in self.answer_type:
                self.no_of_entities_of_right_type = self.no_of_entities_of_right_type + 1
                break
        return self.no_of_entities_of_right_type
    
    def extract_features(self):
        feature = []
        for passage in self.passage_objects:
            passage_features = PassageFeatureExtractor()
            feature.append(passage)
            feature.append(passage_features.no_of_question_keywords_in_passage(self.clean_query, passage.text))
            feature.append(passage_features.longest_sequence_match_with_query(self.query_object.text, passage.text))
            feature.append(passage_features.similarity_measure(self.query_object.text, passage.text))
            feature.append(passage_features.proximity_of_passage(self.clean_query, passage.text))
            self.feature_vector.append(feature)
            feature = []
        return self.feature_vector
    
    def process(self):
        
        feature_vectors = self.extract_features()
        """
        feature vector = [passage_object,keyword_match_%,longest_seq_match,similarity_score,span(proximity)]
         
        Retrieving passage 
        1. filter by keyword match and span(proximity) 
        2. filter by required type of entity
        3. rank/sort the remaining by keyword match, span(proximity) and similarity score respectively
        
        """
        
        """
        filtering 
        level 1 :
            filter by no of keywords, span (proximity score)
        """
        filtered_passage_features = []
        for feature in feature_vectors:
            if  feature[1] > 0.0 and feature[4]:
                filtered_passage_features.append(feature)
                
        """
        level 2 :
            filtering by presence of answer type entity in passage
        """ 
        entity_tagger = AnnotatorPipeline([EntityTagger()])
                
        candidate_passages = [] 
        for filtered_passage_feature in filtered_passage_features:
            entity_tagger.process(filtered_passage_feature[0])
            no_of_entities = self.no_of_entities_of_right_type_in_passage(filtered_passage_feature[0])
            if no_of_entities>0:
                candidate_passages.append(filtered_passage_feature)
                
        
        """
        rank/sort the passages by similarity score
        keyword percent match should be given high priority as length of passages may vary and so will the similarity.
        """    
        candidate_passages.sort(key=lambda x: (x[1],-x[4][0],x[3]),reverse=True)  
    
        return candidate_passages