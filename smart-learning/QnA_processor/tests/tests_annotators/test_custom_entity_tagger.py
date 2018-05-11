

from unittest import TestCase
from QnA_processor.annotators.custom_entity_tagger import predict

class TestCustomEntityTagger(TestCase):
    
    def test_custom_entity_tagger(self):
        print(predict("color blue often use stand things cold"))
        print(predict('south pole located continent antarctica'))
        print(predict("antarctica"))
        print(predict("are four seasons in year winter spring summer autumn."))
        print(predict("places coloured blue on map are often cold"))
        print(predict("are four seasons in year: winter, spring, summer, autumn."))
        print(predict('There are four seasons in a year winter spring summer and autumn'))
        print(predict("are four seasons in year winter spring summer autumn"))
        print(predict("are four seasons in year winter spring summer autumn word seasons means different times year Each season has different weather weather in United States changes depending on where live season Plants trees grass flowers change in different seasons will also see different kinds animals in different seasons"))
