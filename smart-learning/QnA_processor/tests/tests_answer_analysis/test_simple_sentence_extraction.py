'''
Created on Mar 30, 2018

@author: 574965
'''
from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    import mock
from QnA_processor.answer_analysis.simple_sentence_extraction import extract_simple_sentences

class TestSimpleSentenceExtractor(TestCase):
    """
    TO-DO:
        subj-verb-multiple objects(of same type entities)
            eg. sachin played in Australia,India and England
        
        Negations (done only for one verb eg.'he did not even apply to Oxford or Cambridge'.) 
            eg. He did not even bother to give reply to him
            
    """
#     
#     def test_sub_verb_obj(self):
#         sentence_extracted = "Hitler joined the German Workers' Party (DAP)"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,["Hitler joined the German Workers ' Party ( DAP )"])
#         
#     def test_sub_multiple_verbs_obj(self):
#         sentence_extracted = "Hitler joined the German Workers' Party (DAP), the precursor of the NSDAP, and was appointed leader of the NSDAP in 1921"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,["Hitler joined the German Workers ' Party ( DAP ) , the precursor of the NSDAP", 'Hitler joined ,', 'Hitler appointed leader of the NSDAP', 'Hitler appointed in 1921'])
#         
#     def test_multiple_subs_verb_obj(self):
#         sentence_extracted = "Nelson Mandela, Mahatma Gandhi and Adolf Hitler were born in Austria"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,['Nelson Mandela born in Austria', 'Mahatma Gandhi born in Austria', 'Adolf Hitler born in Austria'])
#         
#     def test_multiple_subs_verb_multiple_objs(self):
#         sentence_extracted = "Nelson Mandela, Mahatma Gandhi and Adolf Hitler were born in Austria in 1905"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,['Nelson Mandela born in Austria', 'Nelson Mandela born in 1905', 'Mahatma Gandhi born in Austria', 'Mahatma Gandhi born in 1905', 'Adolf Hitler born in Austria', 'Adolf Hitler born in 1905'])
#         
#     def test_multiple_subs_multiple_verbs_multiple_objs(self):
#         sentence_extracted = "Nelson Mandela,Mahatma Gandhi and Adolf Hitler were born Rolihlahla Mandela on July 18, 1918, in the tiny village of Mvezo, on the banks of the Mbashe River in Transkei, South Africa, moved to Germany in 1913, studied in London and returned in 1945"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,['Nelson Mandela born Rolihlahla Mandela', 'Nelson Mandela born on July 18 , 1918 ,', 'Nelson Mandela born in the tiny village of Mvezo ,', 'Nelson Mandela born on the banks of the Mbashe River in Transkei , South Africa', 'Nelson Mandela born ,', 'Mahatma Gandhi born Rolihlahla Mandela', 'Mahatma Gandhi born on July 18 , 1918 ,', 'Mahatma Gandhi born in the tiny village of Mvezo ,', 'Mahatma Gandhi born on the banks of the Mbashe River in Transkei , South Africa', 'Mahatma Gandhi born ,', 'Adolf Hitler born Rolihlahla Mandela', 'Adolf Hitler born on July 18 , 1918 ,', 'Adolf Hitler born in the tiny village of Mvezo ,', 'Adolf Hitler born on the banks of the Mbashe River in Transkei , South Africa', 'Adolf Hitler born ,',
#                 'Nelson Mandela moved to Germany', 'Nelson Mandela moved in 1913', 'Nelson Mandela moved ,', 
#                 'Mahatma Gandhi moved to Germany', 'Mahatma Gandhi moved in 1913', 'Mahatma Gandhi moved ,', 
#                 'Adolf Hitler moved to Germany', 'Adolf Hitler moved in 1913', 'Adolf Hitler moved ,',
#                 'Nelson Mandela studied in London', 'Mahatma Gandhi studied in London', 'Adolf Hitler studied in London', 
#                 'Nelson Mandela returned in 1945', 'Mahatma Gandhi returned in 1945', 'Adolf Hitler returned in 1945'])
#         
#     def test_obj_on_left_of_subj_verb_obj(self):
#         sentence_extracted = "In 1919, Hitler joined the German Workers' Party (DAP)"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,["Hitler joined the German Workers ' Party ( DAP )",'Hitler joined In 1919'])
#         
#     def test_obj_on_left_of_subj_multiple_verbs_multiple_objs(self):
#         sentence_extracted = "In January 1962, Mandela traveled abroad illegally to attend a conference of African nationalist leaders in Ethiopia, visit the exiled Oliver Tambo in London and undergo guerilla training in Algeria."
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,['Mandela traveled abroad', 'Mandela traveled illegally', 'Mandela traveled to attend a conference of African nationalist leaders in Ethiopia', 'Mandela traveled ,', 'Mandela traveled .', 'Mandela traveled In January 1962', 'Mandela attend a conference of African nationalist leaders in Ethiopia', 'Mandela visit the exiled Oliver Tambo in London', 'Mandela undergo guerilla training in Algeria'])
#         
#     def test_negated_sentence_with_one_verb_negated(self):
#         sentence_extracted = "He was educated at the Harrow prep school, where he performed so poorly that he did not even bother to apply to Oxford or Cambridge."
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         self.assertListEqual(simple_sentences,['He educated at the Harrow prep school ,', 'He educated .', 'He performed so poorly', 'He not bother to apply to Oxford or Cambridge', 'He not bother that'])
#         
# 
#     def test_negated_sentence_with_one_verb_negated2(self):
#         sentence_extracted = "Lee Harvey Oswald, the gunman who assassinated President John F. Kennedy, was later shot and killed by Jack Ruby"
#         simple_sentences = extract_simple_sentences(sentence_extracted)
#         #self.assertListEqual(simple_sentences,['He educated at the Harrow prep school ,', 'He educated .', 'He performed so poorly', 'He not bother to apply to Oxford or Cambridge', 'He not bother that'])
#         print(simple_sentences)
        