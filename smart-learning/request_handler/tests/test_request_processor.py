try:
    from unittest import mock
except ImportError:
    import mock

from unittest import TestCase
from types import ModuleType
from request_handler.request_processor import process_request 

request = {
      "id": "9813047d-b6ed-42bd-8ffe-b5e174f04426",
      "timestamp": "2018-04-20T07:30:51.222Z",
      "lang": "en",
      "result": {
        "source": "agent",
        "resolvedQuery": "read Domain components",
        "action": "",
        "actionIncomplete": False,
        "parameters": {
          "introductorySection": "Domain components"
        },
        "contexts": [],
        "metadata": {
          "intentId": "84f08090-ef43-444e-a5ed-dc0b58ff7deb",
          "webhookUsed": "false",
          "webhookForSlotFillingUsed": "false",
          "intentName": "smartlearning.readout.introductorySection"
        },
        "fulfillment": {
          "speech": "Reading Domain components in intent introductory section",
          "messages": [
            {
              "type": 0,
              "speech": "Reading Domain components in intent introductory section"
            }
          ]
        },
        "score": 1
      },
      "status": {
        "code": 200,
        "errorType": "success",
        "webhookTimedOut": False
      },
      "sessionId": "1d28ac6e-15f4-43fe-a81e-4f1c5fa12d6b"
    }

class TestRequestHandling(TestCase):
    
#     def test_process_request_for_miscellaneous_intent(self):
#         result = process_request(request)
#         expected_result = {'speech': '<speak>This teacher guide consists of an introduction segment, eight lessons along with pausing point & domain review segment.</speak>', 'displayText': 'This teacher guide consists of an introduction segment, eight lessons along with pausing point & domain review segment.', 'data': {'google': {'expect_user_response': True, 'is_ssml': True}}}
#         self.maxDiff = None
#         self.assertEqual(str(result),str(expected_result))
        
    def test_handle_request_for_read_introduction_segment(self):
        result = process_request(request)
        print(result)
    
        