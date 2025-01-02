from flask import Flask, request, jsonify

app = Flask(__name__)

journal_entries = []

@app.route('/submit_journal', methods=['POST'])
def submit_journal():
    data = request.get_json()
    journal_entry = data.get('entry', '')

    if not journal_entry:
        return jsonify({'message': 'No entry provided'}), 400

    journal_entries.append(journal_entry)
    return jsonify({'message': 'Journal entry submitted successfully!', 'entry': journal_entry}), 200

@app.route('/get_journals', methods=['GET'])
def get_journals():
    return jsonify({'entries': journal_entries}), 200

if __name__ == '__main__':
    app.run(debug=True)
