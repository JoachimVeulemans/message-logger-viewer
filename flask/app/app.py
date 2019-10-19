import pandas as pd
import logging
import os
import sys
from flask import Flask, request, jsonify, make_response, Response
from flask_cors import *

origin = os.getenv('ORIGIN')
if origin is None:
    origin = 'http://localhost:4200'

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={
    r"/*": {"origins": ["https://honourlogs.jocawebs.be:443/*"]}})

logging.getLogger('flask_cors').level = logging.DEBUG

@app.route("/")
def hello():
    return "Hello World!!!"

def _build_cors_prelight_response():
    response = make_response()
    response.headers["Access-Control-Allow-Origin"] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['content-type'] = 'application/json'
    response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT,DELETE"
    return response

def _build_cors_actual_response(response):
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 9999
    debug = False

    app.run(host, port, debug)
