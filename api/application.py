from flask import Flask
from flask_cors import CORS
from api.journal.handle_submit_journal import journal_blueprint

app = Flask(__name__)
CORS(app)

# Register the blueprint
app.register_blueprint(journal_blueprint, url_prefix='/journal')

if __name__ == '__main__':
    app.run(port=5000)
