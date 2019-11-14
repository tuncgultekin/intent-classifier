# -*- coding: utf-8 -*-

import os
import argparse
import json
from flask import Flask, request, jsonify
from intent_classifier import IntentClassifier
from intent_api_exceptions import IntentExceptionBase, BodyMissingException, TextMissingException, InvalidTextTypeException, TextEmptyException, InternalServerException

app = Flask(__name__)
model = IntentClassifier()

@app.route('/ready')
def ready():
    if model.is_ready():
        return 'OK', 200
    else:
        return 'Not ready', 423


@app.route('/intent',methods=['post'])
def intent():    
    data = request.get_json(force=True)  

    # Check request parameters
    check_request_body(data)

    try:
        result = model.predict(data['text'])    
        return jsonify(result)    		
    except Exception as e:
        raise InternalServerException(str(e))

def check_request_body(data):
    if (data is None):
        raise BodyMissingException()
        
    if ("text" not in data):
        raise TextMissingException()
        
    if (data['text'] is None or data['text'] == ""):
        raise TextEmptyException()
        
    if (isinstance(data['text'], str) == False):
        raise InvalidTextTypeException()

@app.errorhandler(IntentExceptionBase)
def handle_intent_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
            
def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--model', type=str, required=True, help='Path to model directory')
    arg_parser.add_argument('--port', type=int, default=os.getenv('PORT', 8080), help='Server port number.')
    args = arg_parser.parse_args()
    
    # app.run is a blocking command so there is bug here and model.load must be before app.run
    model.load(args.model)
    app.run(host='0.0.0.0', port=args.port)  
    #model.load(args.model)    


if __name__ == '__main__':
    main()
