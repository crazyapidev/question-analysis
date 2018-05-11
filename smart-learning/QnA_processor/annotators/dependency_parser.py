import logging
logger = logging.getLogger(__name__)

from QnA_processor.annotators.pipeline import Annotator, AnnotationType
from QnA_processor.annotators.datatypes import Dependency
from QnA_processor.annotators import settings

"""
Word_Dependency  = token + pos_tag + dep tag + word_lefts + word_rights + word_head 
"""
class DependencyAnnotator(Annotator):
    def __init__(self, lang='en'):
        super(DependencyAnnotator,self).__init__(AnnotationType.dependency)
        if lang != 'en':
            # We are right now only providing english tokenization
            # and segmentation. But if you need something else, this
            # is a good place to do it.
            raise NotImplementedError
        self.lang = lang

    def __call__(self, doc):
        assert AnnotationType.token in doc.annotations, 'Dependency Annotator can only be run after tokenizer'
        doc.dependencies=en_pos_tag_and_dep(doc)
        doc.annotations.append(AnnotationType.dependency)

def en_pos_tag_and_dep(doc):
    
#     from annotators.nlp_library import NLTKLibrary,SpacyLibrary
    
    nlp_library = settings.NLP_ENGINE.lower() 
    
    dependencies = []
    
    if nlp_library == 'nltk':
        from annotators.nlp_library import NLTKLibrary
        dependencies = NLTKLibrary().tag_pos_and_word_dependency(doc.tokens)
    elif nlp_library == 'spacy':
        from annotators.nlp_library import SpacyLibrary
        dependencies = SpacyLibrary().tag_pos_and_word_dependency(doc.text)
    
    return dependencies
