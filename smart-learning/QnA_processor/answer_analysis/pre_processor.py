
import re
from QnA_processor.annotators.pipeline import AnnotatorPipeline
from QnA_processor.annotators.datatypes import Document
from QnA_processor.annotators.sentencer import SentenceAnnotator
from QnA_processor.annotators.tokenizer import TokenAnnotator
from QnA_processor.annotators.word import WordAnnotator
from QnA_processor.answer_analysis.settings import CUSTOM_STOPWORDS_PATH

tagger = AnnotatorPipeline([SentenceAnnotator(),TokenAnnotator(),WordAnnotator()])

VERBS = ['BES','HVS','MD','VBD','VBG','VBZ','VBN','VB','VBP','VERB']

class PreProcess():
    
    
    def remove_stopwords(self,document):
        clean_document = []
        with open(CUSTOM_STOPWORDS_PATH,'r') as f:
            custom_stopwords = f.read()   
        for word in document.lower().split():
            if word not in custom_stopwords:
                clean_document.append(str(word))
        
        return " ".join(clean_document)
    
    def remove_punctuation(self,old_string):
        new_string = re.sub(r"[-|,|?|!|:|;|'|\|/|_|`|\(|\)]","",old_string)
        return new_string
    
    def pre_process(self,document):

        clean_document = self.remove_punctuation(document)
        clean_document = self.remove_stopwords(clean_document)
        passage_object = Document(id="sample",text=clean_document,raw_text=document)
        tagger.process(passage_object)
        
        for token in passage_object.words:
            try:
                if token.pos in VERBS:
                    passage_tokens = passage_object.text.split()
                    index =  passage_tokens.index(token.token)
                    passage_tokens.pop(index)
                    passage_tokens.insert(index,token.lemma)
                    passage_object.text = " ".join(passage_tokens)  
            except ValueError:
                pass
        return passage_object 
        
    def split_document_into_passages(self,document):
        return document.split('\n\n')
    
    