import React, { useState } from 'react';
import './App.css';
import { getJournalResponse } from './getResponse';

function App() {
  const [input, setInput] = useState('');
  const [journal, setJournal] = useState('');
  let chatGptResponse = 'This is a response from GPT-3';

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = async () => {
    setJournal("Hmmm...");
    try {
        const res = await getJournalResponse(input);
        setJournal(res.message);
    } catch (error) {
        console.error(error);
        setJournal('Error submitting journal');
    }
    setInput('');
};


  return (
    <div className="app-container">
      <h1>Journal App</h1>
      <div className="input-section">
        <textarea 
          value={input} 
          onChange={handleInputChange} 
          placeholder="Write your thoughts..." 
          className="input-area"
        />
        <textarea
          value={chatGptResponse}
          className='input-area'
          inputMode='none'
          readOnly
        />
        <button onClick={handleSubmit} className="submit-btn">Submit</button>
      </div>
      <div className="journal-display">
        {journal ? <p>{journal}</p> : <p>Your journal entry will appear here...</p>}
      </div>
    </div>
  );
}

export default App;