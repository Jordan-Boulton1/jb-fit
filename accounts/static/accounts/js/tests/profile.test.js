/* jshint esversion: 11, jquery: true */
/* global beforeEach, describe, expect, jest, test */

let selectedLogId = null;  // Declare the variable as writable for global access

import '@testing-library/jest-dom';  // Import Jest DOM for enhanced DOM testing capabilities
import { screen } from '@testing-library/dom';  // Import screen utilities from testing-library
import fetchMock from 'jest-fetch-mock';  // Import fetch-mock for mocking fetch requests
import { loadChartData, loadLogHistory } from '../profile.js';  // Import functions to be tested

// Enable fetch mocks to intercept and control fetch requests
fetchMock.enableMocks();

beforeEach(() => {
    // Set up our document body with necessary HTML elements for testing
    document.body.innerHTML = `
        <div>
            <span id="current_weight">(70)</span>  <!-- Simulate current weight display -->
            <canvas id="weightChart"></canvas>  <!-- Simulate chart canvas element -->
            <table id="weightLogsTable">  <!-- Simulate weight logs table -->
                <tbody></tbody>
            </table>
            <div id="deleteConfirmationModal"></div>  <!-- Simulate delete confirmation modal -->
        </div>
    `;

    // Reset selectedLogId to null before each test
    selectedLogId = null;

    // Mock scrollTo normally to prevent actual scrolling during tests
    global.scrollTo = jest.fn();

    // Mock location.reload using Object.defineProperty to avoid reloading the test environment
    Object.defineProperty(window, 'location', {
        writable: true,
        value: {
            ...window.location,
            reload: jest.fn(),  // Mock reload to verify it was called
        },
    });

    // Clear all fetch mock instances and calls to reset state
    fetchMock.resetMocks();
    jest.clearAllMocks();  // Clears any mock calls and instances

    // Mock getContext for canvas to avoid actual rendering issues in tests
    HTMLCanvasElement.prototype.getContext = jest.fn().mockReturnValue({});
});

// Mock the loadChartData function globally to control its behavior in tests
global.loadChartData = jest.fn(() => {
    // Mock implementation of loadChartData
    // Simulate data processing and DOM manipulation if necessary
    const currentWeight = document.getElementById('current_weight').textContent.slice(1, -1);
    const chart = document.getElementById('weightChart');
    chart.innerHTML = '';  // Simulate clearing the chart

    // You can log or set expectations here to test behavior
    console.log('Mock loadChartData called with current weight:', currentWeight);
});

// Test suite for loadChartData function
describe('loadChartData', () => {
    test('fetches data and draws the chart', async () => {
        // Mocking the fetch call to return a valid response
        fetchMock.mockResponseOnce(JSON.stringify([
            { entry_date: '2023-08-30T00:00:00Z', weight: 68 },
            { entry_date: '2023-08-29T00:00:00Z', weight: 67 },
        ]));

        // Mocking Chart.js to avoid rendering issues
        const mockChart = jest.fn();
        window.Chart = mockChart;

        // Mock getContext to avoid actual DOM manipulation
        HTMLCanvasElement.prototype.getContext = jest.fn();

        // Call the actual loadChartData function
        loadChartData();

        // Await for fetch to resolve
        await new Promise(process.nextTick); // Ensure all promises are resolved

        // Check if fetch was called correctly with the correct endpoint
        expect(fetch).toHaveBeenCalledWith('/api/weight-logs-chart');

        // Check if getContext was called correctly
        expect(HTMLCanvasElement.prototype.getContext).toHaveBeenCalledWith('2d');

        // Check if chart was created with correct data
        expect(mockChart).toHaveBeenCalled();
    });
});

// Test suite for loadLogHistory function
describe('loadLogHistory', () => {
    test('fetches data and populates the log history table', async () => {
        // Mocking the fetch call to return a valid response
        fetchMock.mockResponseOnce(JSON.stringify([
            { id: 1, entry_date: '2023-08-30T00:00:00Z', weight: 68 },
            { id: 2, entry_date: '2023-08-29T00:00:00Z', weight: 67 },
        ]));

        // Call the loadLogHistory function
        loadLogHistory();

        // Await for fetch to resolve
        await new Promise(process.nextTick);

        // Check if the fetch was called correctly with the correct endpoint
        expect(fetch).toHaveBeenCalledWith('/api/weight-logs-history');

        // Check if the table was populated correctly by verifying rows
        const rows = screen.getAllByRole('row');
        expect(rows).toHaveLength(2); // Check that there are two rows, one for each log

        // Validate the contents of each row
        expect(rows[0]).toHaveTextContent('30/08/2023');  // Adjust date format based on locale
        expect(rows[0]).toHaveTextContent('68');
        expect(rows[1]).toHaveTextContent('29/08/2023');
        expect(rows[1]).toHaveTextContent('67');
    });
});

// Test suite for deleteWeightLog function
describe('deleteWeightLog', () => {
    test('sets the selected log id and shows confirmation modal', () => {
        // Simulate the deleteWeightLog function behavior
        function deleteWeightLog(logId) {
            selectedLogId = logId;  // Set the selected log ID globally
            const confirmationModal = document.getElementById('deleteConfirmationModal');
            const modal = new global.bootstrap.Modal(confirmationModal);
            modal.show();  // Show the confirmation modal
        }

        // Call the deleteWeightLog function with a log ID
        deleteWeightLog(1);

        // Check if the selected log id is set correctly
        expect(selectedLogId).toBe(1);

        // Check if the Bootstrap modal was initialized correctly with the correct element
        expect(global.bootstrap.Modal).toHaveBeenCalledWith(document.getElementById('deleteConfirmationModal'));

        // Retrieve the modal instance and check if the show method was called
        const modalInstance = global.bootstrap.Modal.mock.results[0].value; // Get the instance returned by Modal()
        expect(modalInstance.show).toHaveBeenCalled();
    });
});

// Test suite for confirmDeleteWeightLog function
describe('confirmDeleteWeightLog', () => {
    test('sends DELETE request and reloads page on successful deletion', async () => {
        // Mock fetch response to simulate successful deletion
        fetchMock.mockResponseOnce('', { status: 200 });

        // Define the confirmDeleteWeightLog function to test
        function confirmDeleteWeightLog() {
            if (selectedLogId) {  // Check if a log has been selected
                const csrfToken = 'mockCsrfToken'; // Mock CSRF token for test purposes
                fetch(`/api/delete-weight-log/${selectedLogId}`, {
                    method: 'DELETE',  // Use the DELETE HTTP method
                    headers: {
                        'X-CSRFToken': csrfToken,  // Include the CSRF token in the headers
                    },
                })
                .then(response => {
                    if (response.ok) {
                        // Scroll to the top before reloading the page
                        window.scrollTo(0, 0);
                        window.location.reload();  // Reload the page to reflect changes
                    } else {
                        console.error('Failed to delete log');  // Log an error if the deletion fails
                    }
                })
                .catch(error => console.error('Error:', error));  // Log any errors during the fetch
            }
        }

        // Define the deleteWeightLog function to test integration with confirmDeleteWeightLog
        function deleteWeightLog(logId) {
            selectedLogId = logId;  // Set the selected log ID globally
            const confirmationModal = document.getElementById('deleteConfirmationModal');
            const modal = new global.bootstrap.Modal(confirmationModal);
            modal.show();  // Show the confirmation modal
        }

        // Call the deleteWeightLog function to select a log for deletion
        deleteWeightLog(1);
        // Call the confirmDeleteWeightLog function to confirm and proceed with deletion
        confirmDeleteWeightLog();

        // Await for fetch to resolve
        await new Promise(process.nextTick);

        // Check if DELETE request was sent with the correct URL and headers
        expect(fetch).toHaveBeenCalledWith('/api/delete-weight-log/1', {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': 'mockCsrfToken',
            },
        });

        // Check if scrollTo and reload methods were called correctly
        expect(global.scrollTo).toHaveBeenCalledWith(0, 0);
        expect(window.location.reload).toHaveBeenCalled();
    });
});
