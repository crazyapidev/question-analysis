from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.annotators.sentencer import en_segment
from QnA_processor.annotators.datatypes import Document
from QnA_processor.answer_analysis.sentence_extraction import SentenceExtraction

class TestSentenceSegmentation(TestCase):

    def test_split_passage_into_sentences(self):
        paragraph = '''Indian Prime Minister Narendra Modi met with Iranian President Hassan Rouhani to discuss bilateral relations in Italy.This happened on 14th February 2018 at 1 p.m IST in the presence of Barrack Obama at saturday morning'''
        expected = [('Indian Prime Minister Narendra Modi met with Iranian President Hassan Rouhani to discuss bilateral relations in Italy.', (0, 136))
('This happened on 14th February 2018 at 1 p.m IST in the presence of Barrack Obama at saturday morning', (136, 237))]
        sentencer = SentenceExtraction(paragraph)
        result = sentencer.split_passage_into_sentences()
        self.assertIn(expected, result)
        

        


