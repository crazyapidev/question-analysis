from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.answer_analysis.sentence_feature_analysis import FeatureMeasure

class TestFeatureMeasure(TestCase):

    def test_longest_sequence_match(self):
        query = "who reputedly appeared to Saint Bernadette Soubirous in 1858"
        candidate_answer = ["Atop the Main Building's gold dome is a golden statue of the Virgin Mary.",
                            "It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858.",
                            "At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary"]
        feature_measure = FeatureMeasure(query,candidate_answer)
        expected_result = candidate_answer[0]
        self.assertEqual (expected_result,feature_measure.longest_sequence_match())
        
    def test_similarity(self):
        query = "who reputedly appeared to Saint Bernadette Soubirous in 1858"
        candidate_answer = ["Atop the Main Building's gold dome is a golden statue of the Virgin Mary.",
                            "It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858.",
                            "At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary"]
        feature_measure = FeatureMeasure(query,candidate_answer)
        expected_result = candidate_answer[0]
        self.assertEqual (expected_result,feature_measure.longest_sequence_match())
        
    def test_keyword_match(self):
        query = "who reputedly appeared to Saint Bernadette Soubirous in 1858"
        candidate_answer = ["Atop the Main Building's gold dome is a golden statue of the Virgin Mary.",
                            "It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858.",
                            "At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary"]
        feature_measure = FeatureMeasure(query,candidate_answer)
        expected_result = candidate_answer[0]
        self.assertEqual (expected_result,feature_measure.longest_sequence_match())
        
        