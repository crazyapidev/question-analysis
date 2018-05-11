

from unittest import TestCase

try:
    from unittest import mock
except ImportError:
    import mock

from QnA_processor.answer_analysis.sentence_extraction import SentenceExtraction

class TestSentenceExtractor(TestCase):
    
#     def test_sentence_extractor_for_LOC_entity(self):
#         query = "Where did Mandela visit Oliver Tombo"
#         clean_passage = "Under Mandela’s leadership  MK launch a sabotage campaign against the government  which have recently declare South Africa a republic and withdraw from the British Commonwealth. In January 1962  Mandela travel abroad illegally to attend a conference of African nationalist leaders in Ethiopia  visit the exile Oliver Tambo in London and undergo guerilla training in Algeria. On August 5  shortly after his return  he be arrest and subsequently sentence to five years in prison for leave the country and incite a 1961 workers’ strike. The following July  police raid an ANC hideout in Rivonia  a suburb on the outskirts of Johannesburg  and arrest a racially diverse group of MK leaders who have gather to debate the merits of a guerilla insurgency. Evidence be find implicate Mandela and other activists  who be bring to stand trial for sabotage  treason and violent conspiracy alongside their associates."
#         raw_passage = "Under Mandela’s leadership, MK launched a sabotage campaign against the government, which had recently declared South Africa a republic and withdrawn from the British Commonwealth. In January 1962, Mandela traveled abroad illegally to attend a conference of African nationalist leaders in Ethiopia, visit the exiled Oliver Tambo in London and undergo guerilla training in Algeria. On August 5, shortly after his return, he was arrested and subsequently sentenced to five years in prison for leaving the country and inciting a 1961 workers’ strike. The following July, police raided an ANC hideout in Rivonia, a suburb on the outskirts of Johannesburg, and arrested a racially diverse group of MK leaders who had gathered to debate the merits of a guerilla insurgency. Evidence was found implicating Mandela and other activists, who were brought to stand trial for sabotage, treason and violent conspiracy alongside their associates."
#         entity_type = "GPE"
#         sentence = "In January 1962  Mandela travel abroad illegally to attend a conference of African nationalist leaders in Ethiopia  visit the exile Oliver Tambo in London and undergo guerilla training in Algeria."
#         extractor = SentenceExtraction(query,entity_type,clean_passage,raw_passage)
#         sent_obj = extractor.process()
#         print (sent_obj.raw_text)
#         self.assertEqual(sent_obj.text,sentence)
        
#     def test_sentence_extractor_for_PERSON_entity(self):
#         query = "Whom did Mandela visit in London"
#         clean_passage = "Under Mandela’s leadership  MK launch a sabotage campaign against the government  which have recently declare South Africa a republic and withdraw from the British Commonwealth. In January 1962  Mandela travel abroad illegally to attend a conference of African nationalist leaders in Ethiopia  visit the exile Oliver Tambo in London and undergo guerilla training in Algeria. On August 5  shortly after his return  he be arrest and subsequently sentence to five years in prison for leave the country and incite a 1961 workers’ strike. The following July  police raid an ANC hideout in Rivonia  a suburb on the outskirts of Johannesburg  and arrest a racially diverse group of MK leaders who have gather to debate the merits of a guerilla insurgency. Evidence be find implicate Mandela and other activists  who be bring to stand trial for sabotage  treason and violent conspiracy alongside their associates."
#         raw_passage = "Under Mandela’s leadership, MK launched a sabotage campaign against the government, which had recently declared South Africa a republic and withdrawn from the British Commonwealth. In January 1962, Mandela traveled abroad illegally to attend a conference of African nationalist leaders in Ethiopia, visit the exiled Oliver Tambo in London and undergo guerilla training in Algeria. On August 5, shortly after his return, he was arrested and subsequently sentenced to five years in prison for leaving the country and inciting a 1961 workers’ strike. The following July, police raided an ANC hideout in Rivonia, a suburb on the outskirts of Johannesburg, and arrested a racially diverse group of MK leaders who had gathered to debate the merits of a guerilla insurgency. Evidence was found implicating Mandela and other activists, who were brought to stand trial for sabotage, treason and violent conspiracy alongside their associates."
#         answer_type = ["PERSON"]
#         sentence = "In January 1962  Mandela travel abroad illegally to attend a conference of African nationalist leaders in Ethiopia  visit the exile Oliver Tambo in London and undergo guerilla training in Algeria."
#         extractor = SentenceExtraction(query,answer_type,clean_passage,raw_passage)
#         sent_obj = extractor.process()
#         print (sent_obj.raw_text)
#         self.assertEqual(sent_obj.text,sentence)
        
#     def test_sentence_extractor_for_EVENT_entity(self):
#         query = "Which are the different kinds of weather"
#         clean_passage = "many different kinds weather. sunny weather cloudy weather windy weather rainy weather stormy weather. weather like outside today live teacher say no matter live earth weather always change hour hour day day. mean weather never stay same. even though weather changes still weather patterns during certain times year. pattern something repeat itself. example weather pattern summer mostly sunny warm. weather patterns may change lot some places very little other places. all depend live earth."
#         raw_passage = "There are many different kinds of weather. There is sunny weather, cloudy weather, windy weather, rainy weather, and stormy weather. What is the weather like outside today where you live? My teacher says that no matter where you live on Earth, the weather is always changing, hour by hour, and day by day. That means the weather never stays the same. But even though the weather changes, there are still weather patterns during certain times of the year. A pattern is something that repeats itself. For example, the weather pattern in the summer is mostly sunny and warm. Weather patterns may change a lot in some places, and very little in other places. It all depends on where you live on Earth."
#         answer_type = ["ENTY:EVENT"]
#         sentence = "There is sunny weather cloudy weather windy weather rainy weather and stormy weather"
#         extractor = SentenceExtraction(query,answer_type,clean_passage,raw_passage)
#         sent_obj = extractor.process()
#         print (sent_obj.raw_text)
#         self.assertEqual(sent_obj.text,sentence)
        
        
    def test_sentence_extractor_for_LOC_entity(self):
        query = "In which season are the animals easy to spot?"
        clean_passage = "after spring come summer. summer hottest season year united states. summer season all plants greenest—full leaves flower fruit. birds bugs other animals easiest spot summer."
        raw_passage = "After spring comes summer. Summer is the hottest season of the year in the United States. Summer is the season in which all the plants are at their greenest—full of leaves, flowers, and fruit. Birds, bugs, and other animals are easiest to spot in the summer."
        answer_type = ["ENTY:EVENT"]
        sentence = "Most of the United States is on the continent of North America although the state of Hawaii is made up of islands located in the Pacific Ocean"
        extractor = SentenceExtraction(query,answer_type,clean_passage,raw_passage)
        sent_obj = extractor.process()
        print (sent_obj.raw_text)
        self.assertEqual(sent_obj.text,sentence)
        
    