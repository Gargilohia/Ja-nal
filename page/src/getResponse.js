

export async function getJournalResponse(journal) {
    const response = await fetch('http://localhost:5000/submit_journal', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({ journal }),
    });
    
    const data = await response.json();
    console.log(data);
    return data;
    }
