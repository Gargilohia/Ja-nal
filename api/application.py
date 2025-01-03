from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit_journal', methods=['OPTIONS', 'POST'])
def submit_journal():
    if request.method == 'OPTIONS':
        # Handle preflight
        response = jsonify({'message': 'CORS preflight passed'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
        return response
    elif request.method == 'POST':
        # Handle actual request
        return jsonify({"message": "Journal submitted successfully!"})

if __name__ == '__main__':
    app.run(port=5000)