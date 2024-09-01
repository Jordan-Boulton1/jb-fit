/* jshint esversion: 11, jquery: true */
/* global bootstrap */
/* global beforeEach, describe, expect, jest, bootstrap, test */

import '@testing-library/jest-dom';  // Import Jest DOM utilities for testing
import { deleteUserAccount, getCookie } from '../edit_profile'; // Adjust path as needed

// Setup to run before each test case
beforeEach(() => {
    // Set up the HTML structure required for the script
    document.body.innerHTML = `
        <div id="deleteConfirmationModal" class="modal"></div>  <!-- Modal element -->
        <button id="promptConfirmDelete">Prompt Delete</button>  <!-- Button to prompt delete -->
        <button id="confirmDeleteButton">Confirm Delete</button>  <!-- Button to confirm delete -->
    `;

    // Clear any previous mocks to ensure each test runs in isolation
    jest.clearAllMocks();
});

// Describe block for grouping tests related to modal and delete functionality
describe('Modal and Delete Functionality', () => {

    // Test case for showing the confirmation modal
    test('showConfirmationModal shows the confirmation modal', () => {
        // Simulate the function behavior for showing the modal
        function showConfirmationModal() {
            var confirmationModal = document.getElementById('deleteConfirmationModal');  // Get the modal element
            var modal = new bootstrap.Modal(confirmationModal);  // Initialize Bootstrap modal
            modal.show();  // Show the modal
        }

        // Call the function to show the modal
        showConfirmationModal();

        // Verify that the Bootstrap modal was initialized with the correct element
        expect(global.bootstrap.Modal).toHaveBeenCalledWith(document.getElementById('deleteConfirmationModal'));

        // Retrieve the modal instance and check if the show method was called
        const modalInstance = global.bootstrap.Modal.mock.results[0].value; // Get the instance returned by Modal()
        expect(modalInstance.show).toHaveBeenCalled();  // Check if the show method was called on the modal instance
    });

    // Test case for deleteUserAccount function
    test('deleteUserAccount makes DELETE request and redirects on success', async () => {
        // Mock fetch to resolve successfully, simulating a successful server response
        global.fetch.mockResolvedValueOnce({ ok: true });

        // Mock getCookie function to return a mock CSRF token
        jest.spyOn(window, 'getCookie').mockReturnValue('mockCsrfToken');

        // Call the deleteUserAccount function
        deleteUserAccount();

        // Await any pending promises to ensure fetch resolves
        await new Promise(process.nextTick);

        // Verify fetch call was made correctly with the DELETE method
        expect(global.fetch).toHaveBeenCalledWith('/api/delete-user', expect.any(Object));

        // Verify the modal was hidden after deletion
        expect(global.$).toHaveBeenCalledWith('#deleteConfirmationModal');
    });

    // Test case for getCookie function
    test('getCookie retrieves the correct cookie value', () => {
        // Set document cookies for testing
        document.cookie = 'csrftoken=test-token; anothercookie=othervalue';

        // Retrieve csrftoken using the getCookie function
        const csrfToken = getCookie('csrftoken');
        expect(csrfToken).toBe('test-token');  // Check if the correct CSRF token is retrieved

        // Retrieve a non-existing cookie
        const nonExisting = getCookie('nonExisting');
        expect(nonExisting).toBe(null);  // Check if the function returns null for non-existing cookies
    });
});
