'''
Created on Feb 26, 2018

@author: 574965
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher
from QnA_processor.annotators import settings

class SentenceFeatureExtractor():
    
    """
    measuring the similarity and key word matching betw
    """
    
    def __init__(self,clean_query,candidate_answers):
        self.clean_query = clean_query 
        self.candidate_answers = candidate_answers
    
    def keyword_match(self):
        
        """
        measuring the percentage of keyword matching between candidate answers
        and query
        """
        clean_query_wordlist = self.clean_query.split()
        keyword_match_percent = []
        for candidate_answer in self.candidate_answers:
            counter = 0
            for word in clean_query_wordlist:
                if word.lower() in candidate_answer.text.lower().split():
                    counter+=1
            percentage_of_match = counter/len(clean_query_wordlist)
            keyword_match_percent.append((candidate_answer,percentage_of_match))
            
        #return max(keyword_match_percent,key=lambda item:item[1])[0]
        return keyword_match_percent           
            
    def similarity_measure(self):
        
        """
        cosine similarity
        """
        
        tfidf_vectorizer=TfidfVectorizer()
        similarity_score = []
        for candidate_answer in self.candidate_answers:
            documents=(self.clean_query.lower(),candidate_answer.text.lower())
            tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
            cs=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)
            similarity_score.append((candidate_answer,cs[0][1]))
        
#         return max(similarity_score,key=lambda item:item[1])[0]     
        return similarity_score
                
    def longest_sequence_match(self):
        
        matching_block_length = []
        for candidate_answer in self.candidate_answers:
            match = SequenceMatcher(None,self.clean_query.lower().split(),candidate_answer.text.lower().split())
            matching_block = match.find_longest_match(0, len(self.clean_query.split()), 0, len(candidate_answer.text.split()))
            matching_block_length.append((candidate_answer,matching_block[2]))
            
#         return  max(matching_block_length,key=lambda item:item[1])[0] 
        return matching_block_length
    

    
    
            
            
            
        
        
        
            