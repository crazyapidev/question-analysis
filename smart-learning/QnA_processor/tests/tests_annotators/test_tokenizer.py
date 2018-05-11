from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.annotators.tokenizer import en_tokenize
from QnA_processor.annotators.datatypes import Document

class TestTokenization(TestCase):

    def check_expected_words_are_in_tokenization(self, text, expected_words):
        doc = Document(id='1',text=text,raw_text=text)
        words = en_tokenize(doc)
        for expected_word in expected_words:
            self.assertIn(expected_word, words)

    def test_point_between_words_is_captured(self):
        text = u"The dog is hungry.The cat is evil."
        expected = [u"dog", u"hungry",u"evil",u"."]
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_hours_are_split(self):
        text = u"It's 3:39 am, what do you want?"
        expected = [u'3',u'39']
        self.check_expected_words_are_in_tokenization(text, expected)
    
    def test_apostrophes_its_split(self):
        text = u"It's 3:39 am, what do you want?"
        expected = [u"It"]
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_question_mark_is_split(self):
        text = u"It's 3:39 am, what do you want?"
        expected = [u"want",u"?"]
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_web_address_is_split(self):
        text = u"Visit http://google.com"
        expected = [u"http",u"://",u"google",u"com"]
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_complex_address_is_split(self):
        text = u"Try with ssh://tom@hawk:2020 and tell me"
        expected = [u"ssh",u"://",u"tom",u"@",u"hawk",u":",u"2020"]
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_Im_arent_and_dont_contraction_apostrophes_are_split(self):
        text = u"I'm ready for you all. Aren't you ready?. Don't you?"
        expected = [u'I', u'Aren', u'Don']
        self.check_expected_words_are_in_tokenization(text, expected)
        
    def test_hyphen_dates_split(self):
        text = u"Back to 10-23-1984 but not to 23/10/1984"
        expected = [u'10', u'23', u'1984']
        self.check_expected_words_are_in_tokenization(text, expected)
 
    def test_slashed_dates_are_split(self):
        text = u"Back to 23/10/1984"
        expected = [u'10',u'23',u'1984']
        self.check_expected_words_are_in_tokenization(text, expected)
 
    def test_hyphened_words_are_split(self):
        text = u"User-friendliness is a must, use get_text."
        expected = [u'User', u'friendliness']
        self.check_expected_words_are_in_tokenization(text, expected)
 
    def test_underscore_words_are_not_split(self):
        text = u"User-friendliness is a must, use get_text."
        expected = [u'get_text']
        self.check_expected_words_are_in_tokenization(text, expected)
 
    def test_colon_is_splitted(self):
        text = u"read what I have to say:I like turtles."
        expected = [u'say', u':', u'I']
        self.check_expected_words_are_in_tokenization(text, expected)
 
    def test_parenthesis_are_split(self):
        text = u"The wolf (starved to death), killed a duck."
        expected = ['(', 'starved', 'to', 'death', '),']
        self.check_expected_words_are_in_tokenization(text, expected)
