document.getElementById('analyzeBtn').addEventListener('click', async function () {
    const description = document.getElementById('description').value;
    const outputDiv = document.getElementById('output');

    if (!description.trim()) {
        outputDiv.innerHTML = 'Please provide a description.';
        return;
    }

    outputDiv.innerHTML = 'Analyzing...';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description }),
        });

        // Check if the response is successful (HTTP status 200)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();

        console.log(result); // Debugging: log the response

        if (result.isRedFlag) {
            outputDiv.innerHTML = `<strong>Red Flag Detected:</strong> ${result.reason}<br><br><strong>Guidance:</strong> ${result.guidance}`;
        } else {
            outputDiv.innerHTML = 'No red flags detected. Everything seems fine.';
        }
    } catch (error) {
        console.error('Error:', error); // Log the error for debugging
        outputDiv.innerHTML = 'Error occurred while analyzing. Please check the server console for details.';
    }
});
