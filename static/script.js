// script.js

// Function to show a loading spinner while waiting for the classification result
function showLoadingSpinner() {
    var spinner = document.getElementById('loading-spinner');
    spinner.style.display = 'block';
}

// Function to hide the loading spinner after receiving the classification result
function hideLoadingSpinner() {
    var spinner = document.getElementById('loading-spinner');
    spinner.style.display = 'none';
}

// Function to handle form submission
function handleSubmit(event) {
    event.preventDefault();
    var complaint = document.getElementById('complaint').value;
    
    // Display loading spinner
    showLoadingSpinner();

    // Send AJAX request to classify complaint
    fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ complaint: complaint })
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading spinner
        hideLoadingSpinner();
        
        // Display result
        var resultContainer = document.getElementById('result-container');
        resultContainer.innerHTML = `<p>Your complaint has been registered. Your ticket no is ${data.ticketNo}. Your complaint will be handled by department: ${data.department}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
        // Hide loading spinner
        hideLoadingSpinner();
    });
}

// Add event listener to form submit
document.getElementById('complaint-form').addEventListener('submit', handleSubmit);
