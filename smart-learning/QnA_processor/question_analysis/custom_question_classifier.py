
import pickle
import numpy as np
from gensim.models import KeyedVectors 
from QnA_processor.question_analysis.utils import average_vector
from QnA_processor.question_analysis.settings import word_vector_path,model_path

class CustomQuestionClassifier():
    
    def __init__(self):
        self.modelpath = model_path
        self.word_vector = KeyedVectors.load_word2vec_format(word_vector_path, binary=False)
        
    def classify_question(self,query):
        self.load_model()
        return self.classifier.predict([np.asarray(average_vector(self.word_vector, query.lower()))])
        
    def load_model(self):
        self.classifier = pickle.load(open(self.modelpath, 'rb'))
        
    