    
    
from QnA_processor.question_analysis.google_question_classifier import GoogleQuestionClassifier
    
def classify_question(query):
    
    try:
        """
        Get answer-type from google autoML classifier 
        (by making POST requests with authorization key)
        """
        question_classifier = GoogleQuestionClassifier()
        answer_type = question_classifier.classify_by_api_call(query)
    except KeyError :
        """
        Get answer-type from google autoML classifier 
         (without authorization key by using google package)
        """
        answer_type = question_classifier.classify_by_package(query)
        
    except:
        """
        Get answer-type from custom question classifier
        """
        from QnA_processor.question_analysis.custom_question_classifier import CustomQuestionClassifier
        question_classifier = CustomQuestionClassifier()
        answer_type = question_classifier.classify_question(query)[0]
        
    return answer_type

# print (classify_question("How many seasons are there in a year"))