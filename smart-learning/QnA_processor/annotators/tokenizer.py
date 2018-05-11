# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from QnA_processor.annotators.pipeline import Annotator,AnnotationType
from QnA_processor.annotators.nlp_library import GoogleNLPLibrary

class TokenAnnotator(Annotator):
    def __init__(self, lang='en'):
        super(TokenAnnotator,self).__init__(AnnotationType.token)
        if lang != 'en':
            # We are right now only providing english tokenization
            # and segmentation. But if you need something else, this
            # is a good place to do it.
            raise NotImplementedError
        self.lang = lang

    def __call__(self, doc):
        if not AnnotationType.token in doc.annotations:
            logger.info("tokenizing: %s" % doc.text)
            doc.tokens=en_tokenize(doc)
            logger.info("tokens: " + str(doc.tokens))
            doc.annotations.append(AnnotationType.token)
        
def en_tokenize(doc):
    
#     from annotators.nlp_library import NLTKLibrary,SpacyLibrary
    from QnA_processor.annotators import settings
    
    nlp_library = settings.NLP_ENGINE.lower() 
    
    tokenAnnotations = []
    
    if nlp_library == 'nltk':
        from QnA_processor.annotators.nlp_library import NLTKLibrary
        tokenAnnotations = NLTKLibrary().tokenization(doc.text)
    elif nlp_library == 'spacy':
        from QnA_processor.annotators.nlp_library import SpacyLibrary
        tokenAnnotations = SpacyLibrary().tokenization(doc.text) 
        
    elif nlp_library == 'google_nlp_api':
        
        tokenAnnotations = GoogleNLPLibrary().tokenization(doc.text)
        
    return tokenAnnotations
