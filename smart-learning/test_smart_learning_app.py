import json
import os
from flask import Flask
from flask import request
from flask import make_response
import logging
from request_handler.request_processor import process_request
import application_logger
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/test-smart-learning-app/test',methods=['POST','GET'])
def test() :
    return "Smart Learning"

@app.route('/test-smart-learning-app', methods=['POST'])
def smartlearning():
    req = request.get_json(silent=True, force=True)
    logger.info("request : %s",json.dumps(req,indent=4))
    res = process_request(req)
    res = json.dumps(res, indent=4)
    logger.info("response : %s",res) 
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__' :
    port = int(os.getenv('PORT', 7500))
    print("Starting app on port "+ str(port))
    app.run(debug=False, port=port, host='0.0.0.0')
