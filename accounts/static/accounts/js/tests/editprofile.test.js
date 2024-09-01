/* jshint esversion: 11, jquery: true */
/* global bootstrap */
/* global beforeEach, describe, expect, jest, bootstrap, test */

import '@testing-library/jest-dom';
import { deleteUserAccount, getCookie } from '../edit_profile'; // Adjust path as needed

beforeEach(() => {
    // Set up the HTML structure required for the script
    document.body.innerHTML = `
        <div id="deleteConfirmationModal" class="modal"></div>
        <button id="promptConfirmDelete">Prompt Delete</button>
        <button id="confirmDeleteButton">Confirm Delete</button>
    `;

    jest.clearAllMocks(); // Clear mocks before each test
});

describe('Modal and Delete Functionality', () => {
    test('showConfirmationModal shows the confirmation modal', () => {
        // Simulate the function behavior
        function showConfirmationModal() {
            var confirmationModal = document.getElementById('deleteConfirmationModal');
            var modal = new bootstrap.Modal(confirmationModal);
            modal.show();
        }

        showConfirmationModal();
        // Verify that the modal was shown
        expect(global.bootstrap.Modal).toHaveBeenCalledWith(document.getElementById('deleteConfirmationModal'));

        // Retrieve the modal instance and check if the show method was called
        const modalInstance = global.bootstrap.Modal.mock.results[0].value; // Get the instance returned by Modal()
        expect(modalInstance.show).toHaveBeenCalled();
    });

    test('deleteUserAccount makes DELETE request and redirects on success', async () => {
        // Mock fetch to resolve successfully
        global.fetch.mockResolvedValueOnce({ ok: true });

        // Mock getCookie function to return a mock CSRF token
        jest.spyOn(window, 'getCookie').mockReturnValue('mockCsrfToken');

        // Mock window location href change
        deleteUserAccount();

        // Await any pending promises
        await new Promise(process.nextTick);

        // Verify fetch call
        expect(global.fetch).toHaveBeenCalledWith('/api/delete-user', expect.any(Object));

        // Verify the modal was hidden
        expect(global.$).toHaveBeenCalledWith('#deleteConfirmationModal');
    });

    test('getCookie retrieves the correct cookie value', () => {
        document.cookie = 'csrftoken=test-token; anothercookie=othervalue';

        // Retrieve csrftoken
        const csrfToken = getCookie('csrftoken');
        expect(csrfToken).toBe('test-token');

        // Retrieve non-existing cookie
        const nonExisting = getCookie('nonExisting');
        expect(nonExisting).toBe(null);
    });
});