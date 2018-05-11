'''
Created on May 9, 2018

@author: 574965
'''

import unittest
from QnA_processor.answer_analysis.question_analyzer import get_answer_type
class TestQuestionClassifier(unittest.TestCase):
    
    def test_google_api_question_classifier(self):
        query = "How many seasons are there in a year"
        answer_type = get_answer_type(query)
        expected = ""
        print (answer_type)