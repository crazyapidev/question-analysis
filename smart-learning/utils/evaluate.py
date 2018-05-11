# -*- coding: utf-8 -*-
'''
Created on Nov 10, 2017

@author: 420169
'''
import sys
import random
import re
from word2number import w2n
import logging
logger = logging.getLogger(__name__)


supporting_list =  ["A+ Work","Amazing","Astonishing","Awesome","BINGO","Bravo","Brilliant","Bueno","Clever","Congratulations","Cool","Excellent","Exceptional","Extraordinary","Fantastic","Good","Good thinking","Great answer","Great job","Hurray","Incredible","Looking good","Magnificient","Marvelous","Neat","Nice job","On target","Outstanding","Perfect","Phenomenal","Remarkable","Right on","Sensational","Spectacular","Stupendous","Super","Super work","Superb","Terrific","That's amazing","That's correct","Tremendous","Very good","Very impressive","Well done"," Winner","Wonderful","You got it"]
no_synonyms = ["negative","nix","absolutely not","by no means","never","no way","not at all","not by any means","false","no","nope"]
yes_synonyms = ["affirmative","amen","fine","good","okay","go","go on","go ahead","ok","true","yea","yeah","all right","aye","beyond a doubt","by all means","certainly","definitely","even so","exactly","gladly","good enough","granted","indubitably","just so","most assuredly","naturally","of course","positively","precisely","sure thing","surely","undoubtedly","unquestionably","very well","willingly","without fail","why not","yep","yes"]

class Validate(object):
    
    def validate(self,user_input,answer,answer_type):
        logger.info("user_input : %s",user_input)
        logger.info("answer : %s",answer)
        logger.info("answer_type : %s",answer_type)
        switch = {
        "dichotomous": validate_dichotomous,
        "numeric": validate_numeric,
        "numericmetric": validate_numeric_distance,
        "word": validate_one_word_answers,
        }
        
        switch_method = switch.get(answer_type.lower(), validate_one_word_answers)
        return switch_method(user_input,answer)


def validate_one_word_answers(user_input,answer):
    
    import nltk, string
    from nltk.corpus import wordnet,stopwords
    from sklearn.feature_extraction.text import TfidfVectorizer
    list3 =answer    
    for idx, val in enumerate(list3):
        list1 = user_input.split()
        list2 = val.split()  
        list = []
        stop_words = set(stopwords.words('english'))
        try :
            for word1 in list1 :
                if word1 not in stop_words:
                    for word2 in list2 :
                        if word2 not in stop_words:
                            wordFromList1 = wordnet.synsets(word1)[0]                        
                            wordFromList2 = wordnet.synsets(word2)[0]
                            s = wordFromList1.wup_similarity(wordFromList2)
                            list.append(s)
        except IndexError:
            pass
    
        if len(list) != 0 and list[0] is not None and max(list) == 1.0  :
            return supporting_list[random.randint(1,len(supporting_list)-1)] + "."
        else :
         
            stemmer = nltk.stem.porter.PorterStemmer()
            remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
            stem_tokens = lambda tokens : [stemmer.stem(item) for item in tokens]
            normalize = lambda text: stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
            vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
            tfidf = vectorizer.fit_transform([user_input, val])
            if (((tfidf * tfidf.T).A)[0,1] <= 1.0 and  ((tfidf * tfidf.T).A)[0,1] >= .9):               
                return supporting_list[random.randint(1,len(supporting_list)-1)] + "."
            elif (((tfidf * tfidf.T).A)[0,1] > .5 and ((tfidf * tfidf.T).A)[0,1] < .9) :                
                return "you are partially right. the correct answer is " + val
            else:               
                continue         
    return "The right answer is " + answer[0]
        

def validate_dichotomous(user_input,answer):
    
    if answer.lower() == "yes" or answer.lower() == "true":
        if user_input.lower() in yes_synonyms:
            return supporting_list[random.randint(1,len(supporting_list)-1)]
        elif user_input.lower() in no_synonyms :
            return "It's actually a true statement" + ". Keep learning !!"
        else :
            return "Please give a valid input. For example: true,yes,false,no,etc.."   
    else:
        if user_input.lower() in no_synonyms:
            return supporting_list[random.randint(1,len(supporting_list)-1)]
        elif user_input.lower() in yes_synonyms :
            return "It's actually a false statement" + ". Keep learning !!"
        else :
            return "Please give a valid input. For example: true,yes,false,no,etc.." 

def validate_numeric(user_input,answer):
    
    try:
        if w2n.word_to_num(str(user_input)) == w2n.word_to_num(str(answer)):
            return supporting_list[random.randint(1,len(supporting_list)-1)]
        else :
            return "It's actually " + answer + ". Keep learning !!"
    except BaseException  as e:
        logger.info("exception : %s",e)
        return "the right answer is " + answer

def validate_numeric_distance(user_input,answer):
    
    from quantulum import parser
    from pint import UnitRegistry,UndefinedUnitError
    
    right_answer = answer
    ureg = UnitRegistry()
    
    try:
        user_input =parser.parse(user_input)
        answer = parser.parse(answer)
        
        unit_input_unit = user_input[0].unit.name.replace("-","_").replace(" ","_") # normalizing of unit names
        answer_unit = answer[0].unit.name.replace("-","_").replace(" ","_") # normalizing of unit names
        quantity1 = ureg.Quantity(user_input[0].value,ureg.parse_expression(str(unit_input_unit))).to('kilometers')
        quantity2 = ureg.Quantity(answer[0].value,ureg.parse_expression(str(answer_unit))).to('kilometers')
         
        percentage_variation = quantity1.magnitude/quantity2.magnitude
        
        if percentage_variation == 1.0 :
            return supporting_list[random.randint(1,len(supporting_list)-1)]
        elif (percentage_variation >=.96 and percentage_variation <= 1.03 ) :
            return supporting_list[random.randint(1,len(supporting_list)-1)] + \
                    " Your answer is in well accepted range. Still if you are curious the exact Value is "+ right_answer
        else:
            return "the right answer is " + right_answer
        
    except UndefinedUnitError:
        return " Distance is expressed in meters,kilometers,miles,astronomical unit,light year"
    except BaseException as e :
        logger.info("exception : %s",e)
        return "the right answer is " + right_answer

    

# print(Validate().validate("1750.403 million miles", "2817 million kilometers", "numericMetric"))
    
