#!/usr/bin/python3
import os
from flask import Flask, jsonify, request, make_response
from file_manager import FileManager
from flask_cors import *
import logging

origin = os.getenv('ORIGIN')
if origin is None:
    origin = 'https://honourlogs.jocawebs.be'

app = Flask(__name__)

CORS(app, supports_credentials=True, resources={
    r"/*": {"origins": ["https://honourlogs.jocawebs.be:443/*"]}})

logging.getLogger('flask_cors').level = logging.DEBUG

file_manager = FileManager("/var/www/public/current/logs.txt", "/var/www/public/deleted/")


@app.route("/")
def hello():
    return "Logger is up & running!"


@app.route("/logs", methods=['GET', 'OPTIONS', 'DELETE'])
def call_get_logs():
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    if request.method == "GET":
        return _build_cors_actual_response(jsonify(file_manager.get_json()))
    if request.method == 'DELETE':
        file_manager.clear()
        return _build_cors_actual_response(jsonify({'success': 'true'}))


@app.route("/log", methods=['POST', 'OPTIONS'])
def call_post_log():
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    if request.method == "POST":
        file_manager.write_line(request.get_json())
        return _build_cors_actual_response(jsonify({'success': 'true'}))


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


if __name__ == "__main__":
    f = open('/var/www/public/current/logs.txt', 'w')
    f.close()
    app.run(debug=True)
