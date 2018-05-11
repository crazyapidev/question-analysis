from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.annotators.sentencer import en_segment
from QnA_processor.annotators.datatypes import Document


class TestSentenceSegmentation(TestCase):

    def check_expected_sentences_are_in_segments(self, text, expected_sentences):
        doc = Document(id='1',text=text,raw_text=text)
        sentences = en_segment(doc)
        self.assertEqual(len(expected_sentences),len(sentences))
        for expected_sentence in expected_sentences:
            self.assertIn(expected_sentence, sentences)

    def test_point_between_words_is_captured(self):
        text = u"The dog is hungry. The cat is evil."
        expected = [(u"The dog is hungry.", (0, 18)), (u"The cat is evil.", (19, 35))]
        self.check_expected_sentences_are_in_segments(text, expected)

    def test_hours_are_not_segmented(self):
        text = u"It's 3:39 am, what do you want?"
        expected = [(u"It's 3:39 am, what do you want?", (0, 31))]
        self.check_expected_sentences_are_in_segments(text, expected)
 
 
    def test_complex_address_is_not_segmented(self):
        text = u"Try with ssh://tom@hawk:2020. If it doesn't work try http://google.com"
        expected = [(u"Try with ssh://tom@hawk:2020.", (0, 29)),(u"If it doesn't work try http://google.com", (30, 70))]
        self.check_expected_sentences_are_in_segments(text, expected)
