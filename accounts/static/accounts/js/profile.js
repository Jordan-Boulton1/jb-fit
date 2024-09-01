/* jshint esversion: 11, jquery: true */
/* global Chart */
/* global bootstrap */

var selectedLogId = null;  // Global variable to store the ID of the selected weight log for deletion

// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function () {
    loadChartData();  // Load the chart data when the page loads
    loadLogHistory();  // Load the weight log history when the page loads

    // Set up the click event for the confirm delete button
    $('#confirmDeleteButton').on('click', () => {
        confirmDeleteWeightLog();  // Call the function to confirm deletion of a weight log
    });
});

// Function to load weight data and render it in a chart
export function loadChartData() {
    var current_weight = document.getElementById('current_weight').textContent.slice(1, -1);  // Get current weight from the page
    let weights = [];  // Array to store weight data
    let labels = [];  // Array to store labels (dates)
    var chart = document.getElementById('weightChart');  // Get the chart element
    chart.innerHTML = '';  // Clear any existing content in the chart element
    var ctx = chart.getContext('2d');  // Get the 2D context for rendering the chart

    // Fetch weight logs data from the API
    fetch("/api/weight-logs-chart")
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            if (current_weight !== null) {
                // Add the current date and current weight as the first entry in the chart
                let currentDate = new Date().toISOString().split('T')[0];  // Get today's date in YYYY-MM-DD format
                labels.push(currentDate);
                weights.push(current_weight);
            }
    
            // Append the rest of the data from the API to the existing arrays
            data.forEach(log => {
                let date = new Date(log.entry_date).toISOString().split('T')[0];  // Convert entry date to YYYY-MM-DD format
                labels.push(date);
                weights.push(log.weight);  // Add each weight log to the weights array
            });

            // Create and render the chart
            var myChart = new Chart(ctx, {
                type: 'line',  // Specify the type of chart
                data: {
                    labels: labels,  // Set the labels for the x-axis
                    datasets: [{
                        label: 'Weight (kg)',  // Label for the dataset
                        data: weights,  // Set the weight data for the chart
                        borderColor: 'rgba(75, 192, 192, 1)',  // Set the color of the line
                        borderWidth: 1,  // Set the width of the line
                        fill: false  // Disable filling under the line
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'time',  // Specify x-axis as time-based
                            time: {
                                unit: 'day',  // Display labels in day units
                                tooltipFormat: 'YYYY-MM-DD'  // Format for the tooltip
                            },
                            title: {
                                display: true,
                                text: 'Date'  // Title for the x-axis
                            },
                            ticks: {
                                callback: function(value) {
                                    return value.split('T')[0];  // Format tick labels
                                }
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Weight (kg)'  // Title for the y-axis
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching weight logs:', error));  // Log errors if fetching fails
}

// Function to load weight log history and display it in a table
export function loadLogHistory() {
    const weightLogsTableBody = document.querySelector('#weightLogsTable tbody');  // Get the table body element
    fetch('/api/weight-logs-history')
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        const weightLogs = data;  // Assign the fetched data to weightLogs
        weightLogsTableBody.innerHTML = ''; // Clear existing rows in the table

        weightLogs.forEach(log => {
            const row = document.createElement('tr');  // Create a new table row
            row.setAttribute('data-id', log.id);  // Set data-id attribute for the row

            // Populate the row with log data and action buttons
            row.innerHTML = `
            <td>${new Date(log.entry_date).toLocaleDateString()}</td>
            <td>${log.weight}</td>
            <td>
                <button class="btn btn-sm btn-primary" onclick="editWeightLog(${log.id})">
                    <i class="fas fa-edit"></i> Edit
                </button>
                <button class="btn btn-sm btn-danger" onclick="deleteWeightLog(${log.id})">
                    <i class="fas fa-trash-alt"></i> Delete
                </button>
            </td>
        `;

            weightLogsTableBody.appendChild(row);  // Append the row to the table body
        });
    });
}

// Function to redirect to the edit page for a specific weight log
function editWeightLog(logId) {
    window.location.href = `/edit-weight-log/${logId}/`;  // Redirect to the edit page
}

// Function to confirm deletion of a selected weight log
function confirmDeleteWeightLog() {
    if (selectedLogId) {  // Check if a log has been selected for deletion
        const csrfToken = getCookie('csrftoken');  // Get CSRF token for the request
        fetch(`/api/delete-weight-log/${selectedLogId}`, {  // Send a DELETE request to the API
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken  // Include CSRF token in the headers
            }
        })
        .then(response => {
            if (response.ok) {
                // Scroll to the top before reloading the page
                window.scrollTo(0, 0);
                location.reload();  // Reload the page to reflect changes
            } else {
                console.error('Failed to delete log');  // Log an error if the deletion fails
            }
        })
        .catch(error => console.error('Error:', error))  // Log any errors during the fetch
        .finally(() => {
            $('#deleteConfirmationModal').modal('hide');  // Hide the confirmation modal after the operation
        });
    }
}

// Function to get a cookie value by name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');  // Split cookies by semicolon
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();  // Trim whitespace from each cookie
            // Check if the cookie starts with the specified name
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  // Decode and get the cookie value
                break;
            }
        }
    }
    return cookieValue;  // Return the cookie value or null if not found
}

// Function to trigger the delete confirmation modal
function deleteWeightLog(logId) {
    selectedLogId = logId;  // Set the selected log ID for deletion
    var confirmationModal = document.getElementById('deleteConfirmationModal');  // Get the modal element
    var modal = new bootstrap.Modal(confirmationModal);  // Initialize the Bootstrap modal
    modal.show();  // Show the modal
}
