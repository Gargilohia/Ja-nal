export const getJournalResponse = async (data) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/submit_journal', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch response');
      }
  
      return await response.json();
    } catch (error) {
      console.error('Error fetching response:', error);
      throw error;
    }
  };
  