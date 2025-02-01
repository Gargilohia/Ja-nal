"""Handles the preflight request for CORS."""
from flask import jsonify

def handle_preflight_request(request):
    """Handles the preflight request for CORS."""
    response = jsonify({'message': 'CORS preflight passed'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'OPTIONS, POST')
    return response