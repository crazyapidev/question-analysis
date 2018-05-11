# -*- coding: utf-8 -*-
from QnA_processor.annotators.utils import strclass
from QnA_processor.annotators.encoding_policy import assert_valid_encoding
from lib2to3.pgen2.token import LEFTSHIFT

class Document(object):
    _attrs = u"id name text raw_text metadata sentences tokens words dependencies entities annotations".split()
    def __init__(self, id, text, raw_text, metadata={}, sentences=[], tokens=[], words=[],dependencies=[], entities=[], annotatitions=[]):
        self.id = id
        self.text = text #lambda / function with no args
        self.raw_text = raw_text
        self.metadata = metadata #dict of field:value
        self.sentences=sentences
        self.tokens=tokens
        self.words=words
        self.entities=entities
        self.dependencies=dependencies
        self.annotations=annotatitions
        
    def __setattr__(self, name, value):
        if name in self._attrs and value is not None:
            object.__setattr__(self, name, value)
        else:
            self.metadata[name]=value

    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(str(x) for x in attrs)

    def __repr__(self):
        return ("<%s id=%s text=%s raw_text=%s metadata=%s>" %
               (strclass(self.__class__), self.id, self.text(), self.raw_text(), self.metadata))

class Answer(object):
    _attrs = u"id name text raw_text metadata sentences tokens words dependencies entities annotations".split()
    def __init__(self, id, text, raw_text, metadata={}, sentences=[], tokens=[], words=[],dependencies=[], entities=[], annotatitions=[]):
        self.id = id
        self.text = text #lambda / function with no args
        self.raw_text = raw_text
        self.metadata = metadata #dict of field:value
        self.sentences=sentences
        self.tokens=tokens
        self.words=words
        self.dependencies=dependencies
        self.entities=entities
        self.annotations=annotatitions
        
    def __setattr__(self, name, value):
        if name in self._attrs and value is not None:
            object.__setattr__(self, name, value)
        else:
            self.metadata[name]=value

    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(str(x) for x in attrs)

    def __repr__(self):
        return ("<%s id=%s text=%s raw_text=%s metadata=%s>" %
               (strclass(self.__class__), self.id, self.text(), self.raw_text(),self.metadata))
        
class Word(object):
    """
    Representation of a tagged word.
    Contains *token*, *lemma*, *pos tag*, *dep tag*, *lefts*, *rights* ,*head*
    """
    _encoding_attrs = u"token lemma pos dep lefts rights head".split() #span
 
    def __init__(self, token, lemma=None, pos=None): #, span to be added if required
        self.token = token
#         self.span = span
        self.pos = pos
        self.lemma = lemma
        
    def __setattr__(self, name, value):
        if name in self._encoding_attrs and value is not None:
            object.__setattr__(self, name, value)
 
    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(str(x) for x in attrs)
 
    def __repr__(self):
        return ("<%s token=%s span=%s >" %
               (strclass(self.__class__), self.token, self.span))

class Dependency(object):
    """
    Representation of a tagged word.
    Contains token,pos tag, dep tag,lefts,rights, head attributes
    """
    _encoding_attrs = u"token pos dep lefts rights head".split() 

    def __init__(self,token, pos, dep, lefts, rights, head): #, span
        self.token = token 
        self.pos = pos
        self.dep = dep
        self._lefts = lefts
        self._rights = rights
        self._head = head


    @property
    def lefts(self):
        return self._lefts
    
    @lefts.setter
    def lefts(self,lefts):
        self._lefts = lefts
        
    @property
    def rights(self):
        return self._rights
    
    @rights.setter
    def rights(self,rights):
        self._rights = rights
        
    @property
    def head(self):
        return self._head
     
    @head.setter
    def head(self,head):
        self._head = head
    
    
    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(x for x in attrs)

    def __repr__(self):
        return ("<%s token=%r >" %
               (strclass(self.__class__), self.token))

    
    
class Entity(object):
    """
    Representation of a tagged entity.
    Contains words, span(start,end), entity_type and dict to add entity attributes
    """
    _encoding_attrs = u"words entity_type span features".split() 

    def __init__(self, words,entity_type,span,features = {}): #, span
        self._words = words
        self.entity_type = entity_type
        self._span = span
        self._features = features

#     def __setattr__(self, name, value):
#         if name in self._encoding_attrs and value is not None:
#             object.__setattr__(self, name, value)
#         else:
#             self.features[name]=value

    @property
    def words(self):
        return self._words
    
    @words.setter
    def words(self,words):
        self._words = words
    
    @property
    def span(self):
        return self._span
     
    @span.setter
    def span(self,span):
        self._span = span
        
    @property
    def features(self):
        return self._features
    
    @features.setter
    def features(self,features):
        self._features = features
    
    
    @property
    def tokens(self):
        return " ".join([x.token for x in self.words])
 
    @property
    def lemmas(self):
        return " ".join([x.lemma for x in self.lemma])


    def __unicode__(self):
        attrs = (getattr(self, name, u"-") for name in self._attrs)
        return u"|".join(x for x in attrs)

    def __repr__(self):
        return ("<%s words=%r span=%s >" %
               (strclass(self.__class__), self.words, self.span))


