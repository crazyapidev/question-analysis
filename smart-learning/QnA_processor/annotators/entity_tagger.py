import logging
logger = logging.getLogger(__name__)

from QnA_processor.annotators.pipeline import Annotator, AnnotationType
from QnA_processor.annotators.custom_entity_tagger import predict
from QnA_processor.annotators.datatypes import Entity
from QnA_processor.annotators import settings


class EntityTagger(Annotator):
    """Trivial Named Entity Recognizer that tags generic named entities"""

    def __init__(self):
       
        super().__init__(AnnotationType.named_entity)

    def __call__(self, doc):
        """entities is a list of Entity.
        """
        doc.entities=tag_entities(doc)
        doc.annotations.append(AnnotationType.named_entity)

def tag_entities(doc):
    
#     from annotators.nlp_library import NLTKLibrary,SpacyLibrary
#     nlp_library = settings.NLP_ENGINE.lower()
    
    
    entities = []
    custom_entities = []
    
#     if nlp_library == 'nltk':
#         entities = NLTKLibrary().tag_generic_entities(doc.text)
#     elif nlp_library == 'spacy':
#         entities = SpacyLibrary().tag_generic_entities(doc.text)
    
    results = predict(doc.text)
    
    for entity,entity_label,entity_span in results:   
        custom_entities.append(Entity(entity,entity_label,entity_span))
        
    entities.extend(custom_entities)     
    return entities