/* jshint esversion: 11, jquery: true */
/* global Chart */
/* global bootstrap */

var selectedLogId = null;

document.addEventListener('DOMContentLoaded', function () {
    loadChartData();
    loadLogHistory();

    // Set up the click event for the confirm delete button
    $('#confirmDeleteButton').on('click', () => {
        confirmDeleteWeightLog();
    });
});

export function loadChartData() {
    var current_weight = document.getElementById('current_weight').textContent.slice(1, -1);
    let weights = [];
    let labels = [];
    var chart = document.getElementById('weightChart');
    chart.innerHTML = '';
    var ctx = chart.getContext('2d');
    fetch("/api/weight-logs-chart")
        .then(response => response.json())
        .then(data => {
            if (current_weight !== null) {
                // Add the current date and current weight as the first entry
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

            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Weight (kg)',
                        data: weights,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                        fill: false
                    }]
                },
                options: {
                    scales: {
                        x: {
                            type: 'time',
                            time: {
                                unit: 'day',
                                tooltipFormat: 'YYYY-MM-DD'
                            },
                            title: {
                                display: true,
                                text: 'Date'
                            },
                            ticks: {
                                callback: function(value) {
                                    return value.split('T')[0];
                                }
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Weight (kg)'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching weight logs:', error));
}

export function loadLogHistory() {
    const weightLogsTableBody = document.querySelector('#weightLogsTable tbody');
    fetch('/api/weight-logs-history')
    .then(response => response.json())
    .then(data => {
        const weightLogs = data;
        weightLogsTableBody.innerHTML = ''; // Clear existing rows

        weightLogs.forEach(log => {
            const row = document.createElement('tr');
            row.setAttribute('data-id', log.id);

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

            weightLogsTableBody.appendChild(row);
        });
    });
}

function editWeightLog(logId) {
    window.location.href = `/edit-weight-log/${logId}/`;
}

function confirmDeleteWeightLog() {
    if (selectedLogId) {
        const csrfToken = getCookie('csrftoken');
        fetch(`/api/delete-weight-log/${selectedLogId}`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => {
            if (response.ok) {
                // Scroll to the top before reloading the page
                window.scrollTo(0, 0);
                location.reload();
            } else {
                console.error('Failed to delete log');
            }
        })
        .catch(error => console.error('Error:', error))
        .finally(() => {
            $('#deleteConfirmationModal').modal('hide');
        });
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteWeightLog(logId) {
    selectedLogId = logId;
    var confirmationModal = document.getElementById('deleteConfirmationModal');
    var modal = new bootstrap.Modal(confirmationModal);
    modal.show();
}
