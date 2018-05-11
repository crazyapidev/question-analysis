# -*- coding: utf-8 -*-

try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase
from types import ModuleType
from request_handler.response_generator import ResponseGenerator
get_response = ResponseGenerator()

request = {
    "id": "a50ea3c6-6f9b-475e-aba8-aa8de519261e",
    "timestamp": "2018-04-24T09:41:31.758Z",
    "lang": "en",
    "result": {
        "source": "agent",
        "resolvedQuery": "read the next section",
        "action": "smartlearningreadoutlessonSegment.smartlearningreadoutlessonSegment-custom",
        "actionIncomplete": False,
        "parameters": {
            "operations" : "next"
        },
        "contexts": [{
                "name": "smartlearningreadoutlessonsegment-followup",
                "parameters": {
                    "lesson_section.original": "read aloud",
                    "lesson_name.original": "lesson 1",
                    "lesson_name": "What�s the Weather Like?",
                    "lesson_section": "Read Aloud",
                    "introductorySection.original": "section",
                    "introductorySection": "section"
                },
                "lifespan": 3
            },
            {
                "name": "operations-followup",
                "parameters": {
                    "lesson_section.original": "read aloud",
                    "lesson_name.original": "lesson 1",
                    "lesson_name": "What's the Weather Like",
                    "lesson_section": "Read Aloud",
                    "lesson_sub_section" : "what's the weather like",
                    "query": "read the section read aloud",
                    "introductorySection.original": "section",
                    "previous_response": "Read Aloud section contains 5 sections, They are Purpose for Listening WHAT'S THE WEATHER LIKE Comprehension Questions Word Work Characteristics Check for Understanding",
                    "intent": "lessonSegment - section - subSection",
                    "introductorySection": "section"
                },
                "lifespan": 1
            },
            {
                "name": "lessonsegment-section-followup",
                "parameters": {
                    "lesson_section.original": "read aloud",
                    "introductorySection.original": "section",
                    "lesson_section": "Read Aloud",
                    "introductorySection": "section"
                },
                "lifespan": 2
            },
            {
                "name": "smartlearningreadoutlessonsegmentsection-followup",
                "parameters": {
                    "lesson_section.original": "read aloud",
                    "introductorySection.original": "section",
                    "lesson_section": "Read Aloud",
                    "introductorySection": "section"
                },
                "lifespan": 2
            }
        ],
        "metadata": {
            "intentId": "e5c852af-dc72-4350-ba37-13627fec46cb",
            "webhookUsed": "true",
            "webhookForSlotFillingUsed": "false",
            "webhookResponseTime": 59,
            "intentName": "smartlearning.operations"
        },
        "fulfillment": {
            "speech": "<speak>Read Aloud section contains 5 sections, They are Purpose for Listening WHAT'S THE WEATHER LIKE Comprehension Questions Word Work Characteristics Check for Understanding</speak>",
            "displayText": "Read Aloud section contains 5 sections, They are Purpose for Listening WHAT'S THE WEATHER LIKE Comprehension Questions Word Work Characteristics Check for Understanding",
            "messages": [{
                "type": 0,
                "speech": "<speak>Read Aloud section contains 5 sections, They are Purpose for Listening WHAT'S THE WEATHER LIKE Comprehension Questions Word Work Characteristics Check for Understanding</speak>"
            }],
            "data": {
                "google": {
                    "is_ssml": True,
                    "expect_user_response": True
                }
            }
        },
        "score": 0.7549868384261669
    },
    "status": {
        "code": 200,
        "errorType": "success",
        "webhookTimedOut": False
    },
    "sessionId": "1cb7acdf-23a3-4c1f-9605-97f4a4a68628"
}

class TestRequestOnOperations(TestCase):
    
    params = request["result"]["parameters"]
    params["intent"] = request["result"]["metadata"]["intentName"]
    context = request["result"]["contexts"]
    
    def test_repeat_request(self):
        self.params["operations"] = "repeat"
        result,context = get_response.generate_response(self.params, self.context)
        print (1,result)
        
    def test_previous_request(self):
        self.params["operations"] = "previous"
        result,context = get_response.generate_response(self.params, self.context)
        print (2,result)
        
    def test_next_request(self):
        self.params["operations"] = "next"
        result,context = get_response.generate_response(self.params, self.context)
        print (3,result)
         
    def test_previous_request_for_first_section(self):
        for context in self.context:
            if context["name"] == "operations-followup":
                context["parameters"]["lesson_sub_section"] = "Purpose for Listening"
        self.params["operations"] = "previous"
        result,context = get_response.generate_response(self.params, self.context)
        print (4,result)
         
    def test_next_request_for_last_section(self):
        for context in self.context:
            if context["name"] == "operations-followup":
                context["parameters"]["lesson_sub_section"] = "Check for Understanding"
        self.params["operations"] = "next"
        result,context = get_response.generate_response(self.params, self.context)
        print (5,result)
    
    
