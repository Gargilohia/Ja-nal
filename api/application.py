from flask import Flask, request, jsonify
from flask_cors import CORS
from fetch_journal_response import fetch_journal_response
from handle_preflight_request import handle_preflight_request

app = Flask(__name__)
CORS(app)  

@app.route('/submit_journal', methods=['OPTIONS', 'POST'])
def submit_journal():
    if request.method == 'OPTIONS':
       return handle_preflight_request(request)

    elif request.method == 'POST':
        data = request.get_json()
        response = fetch_journal_response(data)
        return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
