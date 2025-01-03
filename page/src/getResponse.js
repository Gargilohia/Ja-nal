
export const getJournalResponse = async (journalText) => {
    try {
      const response = await fetch('http://localhost:5000/submit_journal', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ journal: journalText }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      return await response.json();
    } catch (error) {
      console.error('Error fetching response:', error);
      return { error: 'Failed to fetch journal response' };
    }
  };