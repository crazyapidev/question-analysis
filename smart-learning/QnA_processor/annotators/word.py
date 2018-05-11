# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import re

from QnA_processor.annotators.datatypes import Word
from QnA_processor.annotators.pipeline import Annotator, AnnotationType
from QnA_processor.annotators import settings
from QnA_processor.annotators.nlp_library import GoogleNLPLibrary

"""
Word = token + pos_tag + lemma
"""
class WordAnnotator(Annotator):
    def __init__(self, lang='en'):
        super(WordAnnotator,self).__init__(AnnotationType.word)
        if lang != 'en':
            # We are right now only providing english tokenization
            # and segmentation. But if you need something else, this
            # is a good place to do it.
            raise NotImplementedError
        self.lang = lang

    def __call__(self, doc):
        assert AnnotationType.token in doc.annotations, 'Word Annotator can only be run after tokenizer'
        doc.words=en_lemma_and_pos_tag(doc)
        doc.annotations.append(AnnotationType.word)

def en_lemma_and_pos_tag(doc):
    
#     from annotators.nlp_library import NLTKLibrary,SpacyLibrary
    
    nlp_library = settings.NLP_ENGINE.lower() 
    
    words = []
    
    if nlp_library == 'nltk':
        from QnA_processor.annotators.nlp_library import NLTKLibrary
        words = NLTKLibrary().tag_pos_and_lemma(doc.tokens)
    elif nlp_library == 'spacy':
        from QnA_processor.annotators.nlp_library import SpacyLibrary
        words = SpacyLibrary().tag_pos_and_lemma(doc.text)
    elif nlp_library == 'google_nlp_api':
        
        words = GoogleNLPLibrary().tag_pos_and_lemma(doc.text)
    return words
