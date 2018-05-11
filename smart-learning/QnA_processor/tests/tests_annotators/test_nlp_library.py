'''
Created on Feb 20, 2018

@author: 420169
'''
from unittest import TestCase
from QnA_processor.annotators.nlp_library import NLTKLibrary,GoogleNLPLibrary

class TestNLPLibrary(TestCase):
    
    def check_expected_sentences_are_in_segments(self, text, expected_sentences):
        sentences = GoogleNLPLibrary().sentencer(text)
        self.assertEqual(len(expected_sentences),len(sentences))
        for expected_sentences in expected_sentences:
            self.assertIn(expected_sentences, sentences)
    
    
    def test_nltk_sentencer_point_between_words_is_captured(self):
        text = u"The dog is hungry. The cat is evil."
        expected = ["The dog is hungry.", "The cat is evil."]
        self.check_expected_sentences_are_in_segments(text, expected)
        
    def test_nltk_sentencer_hours_are_not_segmented(self):
        text = u"It's 3:39 am, what do you want?"
        expected = [u"It's 3:39 am, what do you want?"]
        self.check_expected_sentences_are_in_segments(text, expected)
 
 
    def test_nltk_sentencer_complex_address_is_not_segmented(self):
        text = u"Try with ssh://tom@hawk:2020. If it doesn't work try http://google.com"
        expected = ["Try with ssh://tom@hawk:2020.","If it doesn't work try http://google.com"]
        self.check_expected_sentences_are_in_segments(text, expected)