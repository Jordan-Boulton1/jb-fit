/* jshint esversion: 11, jquery: true */
/* global Chart */
/* global bootstrap */

var selectedLogId = null;  // Global variable to store the ID of the log to be deleted

// Event listener to execute once the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    loadChartData();  // Load and display the weight data chart
    loadLogHistory();  // Load and display the weight logs in a table

    // Set up the click event for the confirm delete button in the confirmation modal
    $('#confirmDeleteButton').on('click', () => {
        confirmDeleteWeightLog();  // Call the function to confirm deletion of a weight log
    });
});

/**
 * Loads chart data and renders a line chart showing weight changes over time.
 */
export function loadChartData() {
    // Get the current weight from the DOM and remove parentheses from the text
    var current_weight = document.getElementById('current_weight').textContent.slice(1, -1);
    let weights = [];  // Array to hold weight data points
    let labels = [];   // Array to hold date labels for the x-axis
    var chart = document.getElementById('weightChart');  // Get the canvas element for the chart
    chart.innerHTML = '';  // Clear any existing content in the chart
    var ctx = chart.getContext('2d');  // Get the 2D drawing context for the chart

    // Fetch weight log data from the API
    fetch("/api/weight-logs-chart")
        .then(response => response.json())
        .then(data => {
            if (current_weight !== null) {
                // Add the current date and current weight as the first entry in the chart
                let currentDate = new Date().toISOString().split('T')[0];
                labels.push(currentDate);
                weights.push(current_weight);
            }

            // Append the rest of the data from the API to the existing arrays
            data.forEach(log => {
                let date = new Date(log.entry_date).toISOString().split('T')[0];
                labels.push(date);
                weights.push(log.weight);
            });

            // Create and display the line chart using Chart.js
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Weight (kg)',
                        data: weights,
                        borderColor: 'rgba(75, 192, 192, 1)',  // Line color
                        borderWidth: 1,  // Line width
                        fill: false  // Do not fill the area under the line
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'time',  // Use time scale for the x-axis
                            time: {
                                unit: 'day',  // Display data points per day
                                tooltipFormat: 'YYYY-MM-DD'  // Tooltip format for dates
                            },
                            title: {
                                display: true,
                                text: 'Date'  // Label for the x-axis
                            },
                            ticks: {
                                callback: function(value) {
                                    return value.split('T')[0];  // Format tick labels to show only the date
                                }
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Weight (kg)'  // Label for the y-axis
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching weight logs:', error));  // Handle any errors during the fetch
}

/**
 * Loads weight logs history and populates the logs table with data from the server.
 */
export function loadLogHistory() {
    const weightLogsTableBody = document.querySelector('#weightLogsTable tbody');  // Get the table body for weight logs
    fetch('/api/weight-logs-history')  // Fetch weight logs data from the API
        .then(response => response.json())
        .then(data => {
            const weightLogs = data;
            weightLogsTableBody.innerHTML = ''; // Clear existing rows in the table

            // Create table rows for each weight log
            weightLogs.forEach(log => {
                const row = document.createElement('tr');
                row.setAttribute('data-id', log.id);  // Set a data attribute with the log ID

                // Populate the row with log data and buttons for editing and deleting
                row.innerHTML = `
                <td>${new Date(log.entry_date).toLocaleDateString()}</td>
                <td>${log.weight}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="window.editWeightLog(${log.id})">
                        <i class="fas fa-edit"></i> Edit
                    </button>
                    <button class="btn btn-sm btn-danger" onclick="window.deleteWeightLog(${log.id})">
                        <i class="fas fa-trash-alt"></i> Delete
                    </button>
                </td>
                `;

                weightLogsTableBody.appendChild(row);  // Add the row to the table body
            });
        });
}

// Attach functions to the global window object to make them accessible from HTML
window.editWeightLog = function(logId) {
    // Redirect to the edit weight log page for the specified log ID
    window.location.href = `/edit-weight-log/${logId}/`;
};

/**
 * Confirms the deletion of a weight log by sending a DELETE request to the server.
 */
window.confirmDeleteWeightLog = function() {
    if (selectedLogId) {  // Check if a log ID is selected
        const csrfToken = getCookie('csrftoken');  // Get the CSRF token from cookies
        fetch(`/api/delete-weight-log/${selectedLogId}`, {  // Send a DELETE request to the server
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken  // Include the CSRF token in the request headers
            }
        })
        .then(response => {
            if (response.ok) {  // If the request was successful
                // Scroll to the top before reloading the page
                window.scrollTo(0, 0);
                location.reload();  // Reload the page to reflect changes
            } else {
                console.error('Failed to delete log');  // Log an error if deletion failed
            }
        })
        .catch(error => console.error('Error:', error))  // Log any errors during the fetch
        .finally(() => {
            $('#deleteConfirmationModal').modal('hide');  // Hide the delete confirmation modal
        });
    }
};

/**
 * Retrieves the value of a cookie by name.
 * 
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
    let cookieValue = null;  // Initialize cookie value as null
    if (document.cookie && document.cookie !== '') {  // Check if there are any cookies set
        const cookies = document.cookie.split(';');  // Split cookies into an array
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();  // Trim whitespace from each cookie
            if (cookie.substring(0, name.length + 1) === (name + '=')) {  // Check if the cookie name matches
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  // Decode and set the cookie value
                break;
            }
        }
    }
    return cookieValue;  // Return the cookie value or null if not found
}

// Attach deleteWeightLog function to the global window object
window.deleteWeightLog = function(logId) {
    selectedLogId = logId;  // Set the selected log ID for deletion
    var confirmationModal = document.getElementById('deleteConfirmationModal');  // Get the delete confirmation modal element
    var modal = new bootstrap.Modal(confirmationModal);  // Initialize the Bootstrap modal
    modal.show();  // Show the modal to confirm deletion
};
