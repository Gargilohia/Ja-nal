from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/submit_journal', methods=['OPTIONS', 'POST'])
def submit_journal():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight passed'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'OPTIONS, POST')
        return response

    elif request.method == 'POST':
        return jsonify({'message': 'Journal submitted successfully'})

if __name__ == '__main__':
    app.run(port=5000)
