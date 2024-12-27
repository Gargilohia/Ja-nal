# Ja-nal, a Journal App

[Notion Page](https://www.notion.so/Ja-nal-Your-Daily-Journaling-Companion-128c90ab50dd80858f31f854d789f23b)
Inspired by the Japanese katakana style, Ja-nal (ジャーナル) is a user-friendly journal app that brings a fresh twist to daily journaling. 
The mission is to make journaling an enjoyable and engaging habit, encouraging users to reflect, grow, and track their moods every day.

As of now it is a simple journal application built with Flask for the backend and React for the frontend. Users can submit journal entries and retrieve all submitted entries.

## Table of Contents

- [Backend](#backend)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [Submit Journal Entry](#submit-journal-entry)
    - [Get Journal Entries](#get-journal-entries)
- [Frontend](#frontend)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [License](#license)

---

## Backend

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Gargilohia/Ja-nal.git
   ```
   
2. Navigate to the backend folder:

   ```bash
    cd ja-nal/api
    ```

3. Virtual Environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install Flask
   ```
   
### Running the Application
To start the Flask application, run:

   ```bash
   python application.py
   ```

The application will run on localhost:5000.

### API Endpoints

#### Submit Journal Entry
Endpoint: `/submit_journal`
Method: POST
Description: Submit a new journal entry.
cURL Request:

   ```bash
    curl -X POST http://localhost:5000/submit_journal \
    -H "Content-Type: application/json" \
    -d '{"entry": "This is my first journal entry."}'
   ```

#### Get Journal Entries
Endpoint: `/get_journals`
Method: GET
Description: Retrieve all submitted journal entries.
cURL Request:
   ```bash
  curl http://localhost:5000/get_journals
  ```

## Frontend

### Installation

1. Navigate to the frontend folder:

   ```bash
   cd ja-nal/page
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```
   
3. Running the Application
To start the React frontend, run:

   ```bash
   npm start
   ```
The React application will run on localhost:3000.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
This `README.md` provides instructions for setting up and running both the backend (Flask) and frontend (React), including how to interact with the API using `curl` commands.
