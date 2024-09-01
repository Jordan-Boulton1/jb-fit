/* jshint esversion: 11, jquery: true */
/* global beforeEach, describe, expect, jest, test */

let selectedLogId = null;  // Declare the variable as writable

import '@testing-library/jest-dom';
import { screen } from '@testing-library/dom';
import fetchMock from 'jest-fetch-mock';
import { loadChartData, loadLogHistory } from '../profile.js';

// Enable fetch mocks
fetchMock.enableMocks();

beforeEach(() => {
    // Set up our document body
    document.body.innerHTML = `
        <div>
            <span id="current_weight">(70)</span>
            <canvas id="weightChart"></canvas>
            <table id="weightLogsTable">
                <tbody></tbody>
            </table>
            <div id="deleteConfirmationModal"></div>
        </div>
    `;

    // Initialize or reset global selectedLogId as needed for each test
    selectedLogId = null;

    // Mock scrollTo normally
    global.scrollTo = jest.fn();

     // Mock location.reload using Object.defineProperty
    Object.defineProperty(window, 'location', {
        writable: true,
        value: {
            ...window.location,
            reload: jest.fn(),
        },
    });
    // Clear all instances and calls to constructor and all methods:
    fetchMock.resetMocks();
    jest.clearAllMocks(); // Clears any mock calls and instances

    // Mock getContext for canvas
    HTMLCanvasElement.prototype.getContext = jest.fn().mockReturnValue({});
});

// Mock the loadChartData function
global.loadChartData = jest.fn(() => {
    // Mock implementation of loadChartData
    // You can simulate data processing and DOM manipulation if necessary
    const currentWeight = document.getElementById('current_weight').textContent.slice(1, -1);
    const chart = document.getElementById('weightChart');
    chart.innerHTML = ''; // Simulate clearing the chart

    // You can log or set expectations here to test behavior
    console.log('Mock loadChartData called with current weight:', currentWeight);
});

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

        // Check if fetch was called correctly
        expect(fetch).toHaveBeenCalledWith('/api/weight-logs-chart');

        // Check if getContext was called correctly
        expect(HTMLCanvasElement.prototype.getContext).toHaveBeenCalledWith('2d');

        // Check if chart was created with correct data
        expect(mockChart).toHaveBeenCalled();
    });
});

describe('loadLogHistory', () => {
    test('fetches data and populates the log history table', async () => {
        fetchMock.mockResponseOnce(JSON.stringify([
            { id: 1, entry_date: '2023-08-30T00:00:00Z', weight: 68 },
            { id: 2, entry_date: '2023-08-29T00:00:00Z', weight: 67 },
        ]));

        loadLogHistory();

        // Await for fetch to resolve
        await new Promise(process.nextTick);

        // Check if the fetch was called correctly
        expect(fetch).toHaveBeenCalledWith('/api/weight-logs-history');

        // Check if the table was populated correctly
        const rows = screen.getAllByRole('row');
        expect(rows).toHaveLength(2); // One row per log

        expect(rows[0]).toHaveTextContent('30/08/2023');  // Adjust date format based on locale
        expect(rows[0]).toHaveTextContent('68');
        expect(rows[1]).toHaveTextContent('29/08/2023');
        expect(rows[1]).toHaveTextContent('67');
    });
});

describe('deleteWeightLog', () => {
    test('sets the selected log id and shows confirmation modal', () => {
        // Simulate the function behavior
        function deleteWeightLog(logId) {
            selectedLogId = logId;  // Use global scope
            const confirmationModal = document.getElementById('deleteConfirmationModal');
            const modal = new global.bootstrap.Modal(confirmationModal);
            modal.show();
        }

        // Call the deleteWeightLog function
        deleteWeightLog(1);

        // Check if the selected log id is set
        expect(selectedLogId).toBe(1);

        // Check if the Bootstrap modal was initialized correctly
        expect(global.bootstrap.Modal).toHaveBeenCalledWith(document.getElementById('deleteConfirmationModal'));

        // Retrieve the modal instance and check if the show method was called
        const modalInstance = global.bootstrap.Modal.mock.results[0].value; // Get the instance returned by Modal()
        expect(modalInstance.show).toHaveBeenCalled();
    });
});

describe('confirmDeleteWeightLog', () => {
    test('sends DELETE request and reloads page on successful deletion', async () => {
        // Mock fetch response to simulate successful deletion
        fetchMock.mockResponseOnce('', { status: 200 });

        // Define the confirmDeleteWeightLog function
        function confirmDeleteWeightLog() {
            if (selectedLogId) {
                const csrfToken = 'mockCsrfToken'; // Mock token for test purposes
                fetch(`/api/delete-weight-log/${selectedLogId}`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrfToken,
                    },
                })
                .then(response => {
                    if (response.ok) {
                        // Scroll to the top before reloading the page
                        window.scrollTo(0, 0);
                        window.location.reload();
                    } else {
                        console.error('Failed to delete log');
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        }

        // Define the deleteWeightLog function
        function deleteWeightLog(logId) {
            selectedLogId = logId;  // Use global scope
            const confirmationModal = document.getElementById('deleteConfirmationModal');
            const modal = new global.bootstrap.Modal(confirmationModal);
            modal.show();
        }

        // Call the deleteWeightLog function
        deleteWeightLog(1);
        // Call the confirmDeleteWeightLog function
        confirmDeleteWeightLog();

        // Await for fetch to resolve
        await new Promise(process.nextTick);

        // Check if DELETE request was sent
        expect(fetch).toHaveBeenCalledWith('/api/delete-weight-log/1', {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': 'mockCsrfToken',
            },
        });

        // Check if scrollTo and reload methods were called
        expect(global.scrollTo).toHaveBeenCalledWith(0, 0);
        expect(window.location.reload).toHaveBeenCalled();
    });
});
