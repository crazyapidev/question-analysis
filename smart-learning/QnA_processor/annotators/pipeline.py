import logging
from enum import Enum

logger = logging.getLogger(__name__)

class AnnotationType(Enum):
    sentence=1
    token=2
    word=3
#     dependency = 3
    named_entity=3


class AnnotatorPipeline(object):
    
    def __init__(self, annotators):
        self.annotators = annotators

    def annotate(self, annotator, doc):
        logger.info('Initializing annotator pipeline %s', annotator)
        annotator(doc)

    def process(self, doc):
        for annotator in self.annotators:
            logger.info('Processing Query %s', doc.id)
            self.annotate(annotator, doc)


class Annotator(object):
    def __init__(self, annotation_type):
        self.type=annotation_type
    
    def __call__(self, doc):
        # You'll have to:
        # - Check if the document satisfies pre-conditions, and if not, do nothing
        # - Explicitly store pre process results on the document
        raise NotImplementedError
