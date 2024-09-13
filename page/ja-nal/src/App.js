import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [journal, setJournal] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = () => {
    setJournal(input);
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
        <button onClick={handleSubmit} className="submit-btn">Submit</button>
      </div>
      <div className="journal-display">
        {journal ? <p>{journal}</p> : <p>Your journal entry will appear here...</p>}
      </div>
    </div>
  );
}

export default App;