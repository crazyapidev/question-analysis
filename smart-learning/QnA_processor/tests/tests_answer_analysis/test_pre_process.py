from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.answer_analysis.pre_processor import PreProcess


class TestPreProcess(TestCase):
    
    def test_query_pre_process(self):
        query = "Who is hitler married to"
        excepted_processed_query = "Who be hitler marry to"
        process = PreProcess()
        processed_query = process.pre_process(query)
        self.assertEqual(processed_query.text,excepted_processed_query)
        
    def test_passage_pre_precess(self):
        passage = "Summer is the hottest season of the year in the United States.Summer is the season in which all the plants are at their greenest-full of leaves, flowers, and fruit.Birds, bugs, and other animals are easiest to spot in the summer"
        excepted_processed_passage = "Summer be the hottest season of the year in the United States.Summer be the season in which all the plants be at their greenest full of leaves  flowers  and fruit.Birds  bugs  and other animals be easiest to spot in the summer"
        process = PreProcess()
        processed_passage = process.pre_process(passage)
        self.assertEqual(processed_passage.text,excepted_processed_passage)
        
        