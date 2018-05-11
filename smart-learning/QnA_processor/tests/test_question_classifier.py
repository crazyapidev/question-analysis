from unittest import TestCase
from QnA_processor.question_analysis.question_classifier import classify_question

try:
    from unittest import mock
except ImportError:
    import mock


class TestQuestionClassifier(TestCase):
    
    def test_classify_question(self):
        query = "What forms when snow and ice melt"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question2(self):
        query = "What do farmers harvest in autumn"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question3(self):
        query = "What is on the ground during the winters"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question4(self):
        query = "Where is US located"
        expected_answer_type = 'LOC:other'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question5(self):
        query = "Which animal sleeps during the winters"
        expected_answer_type = 'ENTY:animal'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question6(self):
        query = "What color on the map represents hot areas"
        expected_answer_type = 'ENTY:color'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question7(self):
        query = "How many weeks in a month"
        expected_answer_type = 'NUM:count'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question8(self):
        query = "Which is the warmest season of the year"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question9(self):
        query = "What types of weather are experienced by people?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question10(self):
        query = "What does the color blue on the map usually stand for?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question11(self):
        query = "What does the color red on the map usually stand for?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question12(self):
        query = "In which continent is the South Pole located?"
        expected_answer_type = 'LOC:other'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question13(self):
        query = "In which continent is the North Pole located?"
        expected_answer_type = 'LOC:other'
        self.assertEqual(expected_answer_type,classify_question(query))
    
    def test_classify_question14(self):
        query = "What are the plants full of during the summer season?"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))

    def test_classify_question15(self):
        query = "In which season are the animals easy to spot?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
    
    def test_classify_question16(self):
        query = "What is the land covered by at the North and South Poles?"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question17(self):
        query = "What are the different kinds of weather?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question18(self):
        query = "What is the North and South Pole full of?"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question19(self):
        query = "What are the four seasons of the year?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question20(self):
        query = "What is the ground full of during the winters?"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question21(self):
        query = "In which season are usually many baby animals born?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question22(self):
        query = "In which season are birds, bugs and other animals easy to spot?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question23(self):
        query = "In which season do the farmers harvest their fruits and vegetables?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question24(self):
        query = "In which season do the birds fly south?"
        expected_answer_type = 'ENTY:event'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question25(self):
        query = "What do the farmers harvest in the autumn season?"
        expected_answer_type = 'ENTY:food'
        self.assertEqual(expected_answer_type,classify_question(query))
        
    def test_classify_question26(self):
        query = "What is harvested in the autumn season?"
        expected_answer_type = 'ENTY:product'
        self.assertEqual(expected_answer_type,classify_question(query))
        