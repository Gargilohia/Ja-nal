from flask import Blueprint, request, jsonify
from journal.fetch_journal_response import fetch_journal_response
from journal.handle_preflight_request import handle_preflight_request

# blueprint for journal-related routes
journal_blueprint = Blueprint('journal', __name__)

@journal_blueprint.route('/submit', methods=['OPTIONS', 'POST'])
def submit_journal():
    if request.method == 'OPTIONS':
        return handle_preflight_request(request)

    elif request.method == 'POST':
        data = request.get_json()
        response = fetch_journal_response(data)
        return jsonify(response)