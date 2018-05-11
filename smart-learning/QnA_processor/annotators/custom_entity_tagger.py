'''
Created on Apr 9, 2018

@author: 574965
'''
import spacy
import os
import joblib
from QnA_processor.annotators.settings import  CUSTOM_ENTITY_MODEL_PATH

nlp = spacy.load('en_core_web_md')

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def predict(utterance):
    lstenty=[]
    valuelist=[]
    try:
        tagged = []
        finallist = []
        parsed = nlp(utterance)
        for i in range(len(parsed)):
            
            tagged.append((str(parsed[i]),parsed[i].tag_))
        finallist.append(tagged)
        test = [sent2features(s) for s in finallist]
        
        if(os.path.isfile(CUSTOM_ENTITY_MODEL_PATH)):
            crf = joblib.load(CUSTOM_ENTITY_MODEL_PATH)
        else:
            return {'success':False,'message':'Please Train the model first'}
        predicted = crf.predict(test)
        entityList = extractEntities(predicted[0],tagged)
        for keys in entityList:   
            for values in entityList[keys]:
                if values in valuelist:
                    my_dict = {i:valuelist.count(i) for i in valuelist}
                    valuelist.append(values)
                    #print(my_dict[values])
                    start_index=find_nth(utterance,values,my_dict[values]+1)
                    end_index=start_index + len(values)            
                    lstenty.append((values,keys,(start_index,end_index)))
                else:
                    valuelist.append(values)            
                    start_index = utterance.find(values)
                    end_index = start_index + len(values)        
                    lstenty.append((values,keys,(start_index,end_index)))
        #print(lstenty)       
        return {'success':True,'entitiesPredicted':lstenty}['entitiesPredicted']
    except Exception as ex:
        return {'success':False,'message':'Error while pediction - '+str(ex)}


    
def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],        
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True
        
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True
                
    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    #print([label for token, postag, label in sent])
    return [label for token, postag, label in sent]

def extractEntities(predicted,tagged):
    rslt = {}
    label=''
    for i in range(len(predicted)):
        #print(y_pred[0][j])
        if predicted[i].startswith('U-'):
            label = tagged[i][0]
            try:
                rslt[predicted[i][2:]].append(label)
            except:
                rslt[predicted[i][2:]] = [label]
            label=''
            continue
        if predicted[i].startswith('B-'):
            label += tagged[i][0]+" "
        if predicted[i].startswith('I-'):
            label += tagged[i][0]+" "
        if predicted[i].startswith('L-'):
            label += tagged[i][0]
            try:
                rslt[predicted[i][2:]].append(label)
            except:
                rslt[predicted[i][2:]] = [label]
            label=''
            continue
    return rslt

