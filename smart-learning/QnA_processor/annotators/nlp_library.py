# -*- coding: utf-8 -*-
"""
Abstract Base Classes(ABC) for NLP Engines
"""
from abc import abstractmethod
from QnA_processor.annotators.datatypes import Word,Entity #,Dependency
import json
import requests
# from _pyio import __metaclass__

_penn_to_morphy_tag = {}

def penn_to_morphy_tag(tag):
    for penn, morphy in _penn_to_morphy_tag.iteritems():
        if tag.startswith(penn):
            return morphy
    return None

##############################################
# ABC for NLP Library
##############################################

class NLPLibrary (object):
#     __metaclass__ = ABCMeta

    
    @abstractmethod
    def sentencer(self,text):
        """ Sentence Segmentation """
        raise NotImplemented
    
    @abstractmethod
    def tokenization(self,text):
        """ Implement tokenization Logic """
        raise NotImplemented
    
    @abstractmethod
    def tag_pos_and_lemma(self,tokens):
        """ word = token + POS + Lemma """
        raise NotImplemented
    
    @abstractmethod
    def tag_generic_entities(self,text):
        raise NotImplemented
    
#     @abstractmethod
#     def lemma(self,token):
#         """Implement Lemmatization """
#         raise NotImplemented



###############################################
# NLTK subclasses
###############################################

class NLTKLibrary(NLPLibrary):
    
    import nltk
    from nltk.tokenize import PunktSentenceTokenizer
    from nltk import WordPunctTokenizer,pos_tag
    from nltk import corpus
    
    def __init__(self):
        if not self.nltk.data.path:
            raise EnvironmentError('nltk data path not set')
        
        self.sentencer_segmenter = self.PunktSentenceTokenizer()
        self.tokenizer = self.WordPunctTokenizer()
    
    def sentencer(self,text):
        """ 
        sentence segmenter  
        """
        for i, j in self.sentencer_segmenter.span_tokenize(text):
            yield i, j, text[i:j]
    
    def tokenization(self,text):
        """ 
        Tokenize a text into a sequence of alphabetic and
        non-alphabetic characters, using the regexp ``\w+|[^\w\s]+``. 
        """
        tokenAnnotations=[]
        
        for i,j in self.tokenizer.span_tokenize(text):
            tokenAnnotations.append(text[i:j])
        
        return tokenAnnotations
    
    def tag_pos_and_lemma(self,tokens):
        """ POS Tagging and Lemma """
        _penn_to_morphy_tag = {}
        
        if not _penn_to_morphy_tag:
            _penn_to_morphy_tag = {
                u'NN': self.nltk.corpus.reader.wordnet.NOUN,
                u'JJ': self.nltk.corpus.reader.wordnet.ADJ,
                u'VB': self.nltk.corpus.reader.wordnet.VERB,
                u'RB': self.nltk.corpus.reader.wordnet.ADV,
            }

        tags = self.nltk.pos_tag(tokens) #token for (token,(start,end)) in
    
        words = []
        i=0
        for text, pos in tags:
            word = Word(text) # , tokens[i][1],tokens = [(token_text,(start,end))]
            # Eliminates stuff like JJ|CC
            # decode ascii because they are the penn-like POS tags (are ascii).
            word.pos = pos.split("|")[0]
            
            if word.pos in _penn_to_morphy_tag.keys():
                mtag = _penn_to_morphy_tag[word.pos]
            else:
                mtag = self.nltk.corpus.reader.wordnet.NOUN
    
            
            lemma = self.corpus.wordnet._morphy(word.token, pos=mtag)
            if len(lemma)==0:
                word.lemma = word.token.lower()
            else:
                word.lemma = lemma[0]
    
            words.append(word)
            i+=1
        return words
    
    def tag_generic_entities(self,text):
        pass
    
#     def lemma(self,token):
#         """Implement Lemmatization """
#         pass


###############################################
# Spacy NLP Engine
###############################################

class SpacyLibrary(NLPLibrary):
    import spacy
    
    def __init__(self):
        self.nlp =  self.spacy.load('en_core_web_lg')
    
    def sentencer(self,text):
        """ Sentence Segmentation returns list of sentences for given input passage"""
        
        doc = self.nlp(text)
        
        for sent in doc.sents:
            yield sent.start_char,sent.end_char,text[sent.start_char:sent.end_char]
    
    def tokenization(self,text):
        """
        Tokenize a text into a sequence of alphabetic and
        non-alphabetic characters, using the regexp ``\w+|[^\w\s]+``. 
        """
        
        doc = self.nlp(text)
        
        tokenAnnotations=[]
        
        for token in doc:
            tokenAnnotations.append(token.text)
        
        return tokenAnnotations
    
    def tag_pos_and_lemma(self,text):
        """ POS Tagging """
        
        doc = self.nlp(text)
        words = []
        
        for token in doc:
            word = Word(token.text)
            word.pos = token.tag_
            word.lemma = token.lemma_
            words.append(word)
        return words
    
    def tag_pos_and_word_dependency(self,text):
        
        """ Dependency Tagging """
        
        doc = self.nlp(text)
        dependencies = []
        
        for token in doc:
            word = Dependency(token.text,token.tag_,token.dep_,token.lefts,token.rights,token.head)
            dependencies.append(word)
        return dependencies
    
    def tag_generic_entities(self,text):
        
        """ NER tagging """
        
        doc = self.nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append(Entity(ent.text,ent.label_,(ent.start_char,ent.end_char)))
        return entities
#     def lemma(self,token):
#         """Implement Lemmatization """
#         pass
    
class GoogleNLPLibrary():
    
    # def __init__(self):
        
    #    "Not Implemented"
    
    def get_google_nlp_api_response_json(self):
        
        with open("D:/learning_assistant/content_for_code/googleNLPAPI_response.json",'r') as file:
            data = file.read()
            return json.loads(data) 
        
    def tag_by_api_call(self,text):
        
        url = "https://language.googleapis.com/v1/documents:analyzeSyntax"
        querystring = {"key":"AIzaSyDElMxqhv85vE2C3mhWR2i4hLpSWEIGLUo"}
        proxies = {
            'http': 'http://574965:Mar27%402018%23@proxy.cognizant.com:6050',
            'https': 'https://574965:Mar27%402018%23@proxy.cognizant.com:6050',
                   }

        payload = {
              "encodingType": "UTF8",
              "document": {
                "type": "PLAIN_TEXT",
                "content": text
              }
            }
        
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "ebfea716-f0ff-1a5d-f304-5b514e4d90b8"
            }
        
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring,proxies=proxies)
        return json.loads(response.text)  
        
    def tag_by_google_natural_language_package(self):
#         from google.cloud import language
#         from google.cloud.language import enums
#         from google.cloud.language import types
        raise ("Not Implemented")
         
    def sentencer(self,text):
        response = self.tag_by_api_call(text)
#         response = self.get_google_nlp_api_response_json() 
        sentences = response["sentences"]
        for sentence in sentences:
            sent_text = sentence["text"]["content"]
            sent_start_char = sentence["text"]["beginOffset"]
            sent_end_char = sent_start_char + len(sent_text)
            yield sent_start_char,sent_end_char,sent_text
    
    def tokenization(self,text):
        tokens = []
        response = self.tag_by_api_call(text)
#         response = self.get_google_nlp_api_response_json() 
        for token in response["tokens"]:
            tokens.append(token["text"]["content"])
        
        return tokens
    
    def tag_pos_and_lemma(self,text):
        words = []
        response = self.tag_by_api_call(text)
#         response = self.get_google_nlp_api_response_json() 
        for token in response["tokens"]:
            word = Word(token["text"]["content"])
            word.pos = token["partOfSpeech"]["tag"]
            word.lemma = token["lemma"]
            words.append(word)
        return words
    
    def tag_generic_entities(self,text):
        pass
 
# if __name__ == "__main__":
#     nlp_library = GoogleNLPLibrary()
#     text = "Summer is the hottest season"
#     words = nlp_library.tag_pos_and_lemma(text)
#     
#     for word in words:
#         print(word.token)   
    
