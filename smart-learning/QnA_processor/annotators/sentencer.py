# -*- coding: utf-8 -*-
from QnA_processor.annotators.pipeline import Annotator, AnnotationType
from QnA_processor.annotators import settings
from QnA_processor.annotators.nlp_library import GoogleNLPLibrary

class SentenceAnnotator(Annotator):
    def __init__(self, lang='en'):
        super(SentenceAnnotator,self).__init__(AnnotationType.sentence)
        if lang != 'en':
            # We are right now only providing english tokenization
            # and segmentation. But if you need something else, this
            # is a good place to do it.
            raise NotImplementedError
        self.lang = lang

    def __call__(self, doc):        
        if not AnnotationType.sentence in doc.annotations:
            doc.sentences=en_segment(doc)
            doc.annotations.append(AnnotationType.sentence)
        
def en_segment(doc):
    """
    segments a string `text` interpreted as english text.
    Returns:
        - a dict with sentence as key and value as span
    """
#     from annotators.nlp_library import NLTKLibrary,SpacyLibrary
    
    nlp_library = settings.NLP_ENGINE.lower() 
    
    if nlp_library == 'nltk':
        from QnA_processor.annotators.nlp_library import NLTKLibrary
        sentence_segmenter = NLTKLibrary().sentencer(doc.text)
        
    elif nlp_library == 'spacy':
        from QnA_processor.annotators.nlp_library import SpacyLibrary
        sentence_segmenter = SpacyLibrary().sentencer(doc.text)
        
    elif nlp_library == 'google_nlp_api':
        
        sentence_segmenter = GoogleNLPLibrary().sentencer(doc.text)
    
    sentences = []
    
    for sentence_i, sentence_j, sentence in sentence_segmenter:
        if sentence_i == sentence_j:
            continue
        sentences.append((sentence,(sentence_i,sentence_j)))
    return sentences

    
