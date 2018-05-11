import json
import operator
from QnA_processor.question_analysis.settings import SYNONYMS_PATH

"""
Converting word to vector using gensim Word2Vec/KeyedVec
Word projections(PCA(dimensionality reduction))
loading word vectors from gensim to create feature vectors for words in questions 
"""
vector_dim = 50

def average_vector2(dictionary, question):
    cnt = 0
    s = [0]*vector_dim
    for w in question.split():
        w = w.lower()
        cnt += 1
        try:
            s = map(operator.add, dictionary[w], s)
        except KeyError:
            cnt -= 1
    if cnt == 0:
        return s
    return [elem/float(cnt) for elem in s]

def average_vector(dictionary, question):
    splitted = question.split()
    s = [0]*vector_dim
    cnt = 2.0
    try:
        if (len(splitted) == 0):
            return s
        else:
            s = map(operator.add, dictionary[splitted[0].lower()], s)
            if (len(splitted) <= 1):
                return s
            s = map(operator.add, dictionary[splitted[1].lower()], s)
            if (splitted[0].lower() == 'what' and splitted[1].lower() == 'is'):
                return average_vector2(dictionary, question)
            return [elem/cnt for elem in s]         
    except KeyError:
        if len(splitted)>2:
            s = map(operator.add, dictionary[splitted[2].lower()], s)
            return [elem/cnt for elem in s] 
        return s 

def rephrase_query_with_synonyms(query):
    synonyms_dict = {}
    with open(SYNONYMS_PATH,'r') as f:
        synonyms_dict = json.loads(f.read())
    new_query=''       
    for token in query.split():
        c=0
        for key in synonyms_dict.keys():
            if token in synonyms_dict[key]:
                if c==0:
                    new_query = new_query + token + ' ' + key + ' '
                    c = c+1
                else:
                    new_query = new_query + key + ' '
        if c==0:
            new_query = new_query + token + ' '
    return new_query
    
    