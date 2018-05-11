from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher
import itertools

class PassageFeatureExtractor():
    
    def __init__(self):
        self.no_of_question_keywords = 0
    
    
    def no_of_question_keywords_in_passage(self,query,passage):
        for word in query.lower().split():
            if word in passage.lower().replace(".","").split():
                self.no_of_question_keywords += 1
        feature_value = self.no_of_question_keywords/float (len(query.split()))
        return feature_value
    
    def longest_sequence_match_with_query(self,query,passage):
        match = SequenceMatcher(None,query.lower().split(),passage.lower().replace(".","").split())
        matching_block = match.find_longest_match(0, len(query.split()), 0, len(passage.split()))
        return matching_block[2]
    
    
    def similarity_measure(self,query,passage):
        
        """
        cosine similarity
        """
        tfidf_vectorizer=TfidfVectorizer()
        documents=(query.lower(),passage.lower().replace(".",""))
        tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
        cs=cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)
        return  cs[0][1]  
    
    def proximity_of_passage(self,query,passage):
        words = passage.lower().replace(".","").split()
        query_words = query.lower().split()
        proximities = []
        for i in range(len(query_words)):
            first_word_to_look_up = query_words[i]
            for j in range(i+1,len(query_words)):
                second_word_to_look_up = query_words[j]
                proximity = self.get_distance( first_word_to_look_up,second_word_to_look_up,words)
                if proximity:
                    proximities.append(proximity)
                    
        if proximities:
            return min(proximities, key = lambda t: t[0])
        else :
            return None   
                
    def get_distance(self, word1,word2,words):
        if word1 in words and word2 in words:
            word1_indexes = [index for index, value in enumerate(words) if value == word1]    
            word2_indexes = [index for index, value in enumerate(words) if value == word2]    
            distances = [(abs(item[0] - item[1]),item[0],item[1]) for item in itertools.product(word1_indexes, word2_indexes)]
            return  min(distances, key = lambda t: t[0])
    
    
    