/* jshint esversion: 11, jquery: true */
/* global bootstrap */

// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Set up the click event listener for the button that prompts the delete confirmation
    $('#promptConfirmDelete').on('click', () => {
        showConfirmationModal();  // Show the delete confirmation modal when the button is clicked
    });

    // Set up the click event listener for the confirm delete button in the modal
    $('#confirmDeleteButton').on('click', () => {
        deleteUserAccount();  // Call the function to delete the user account when confirmed
    });

    // Handle the event when the delete confirmation modal is hidden
    $('#deleteConfirmationModal').on('hidden.bs.modal', function () {
        $('body').removeClass('modal-open');  // Ensure the body class 'modal-open' is removed to fix scrolling issues
        $('.modal-backdrop').remove();  // Remove the backdrop manually in case it wasn't removed automatically
    });
});

// Function to show the delete confirmation modal
export function showConfirmationModal() {
    // Get the modal element from the DOM
    var confirmationModal = document.getElementById('deleteConfirmationModal');
    // Initialize the Bootstrap modal using the modal element
    var modal = new bootstrap.Modal(confirmationModal);
    // Show the modal to the user
    modal.show();
}

// Function to delete the user account
export function deleteUserAccount(){
    // Retrieve the CSRF token from the cookies
    const csrfToken = getCookie('csrftoken');

    // Send a DELETE request to the server to delete the user account
    fetch(`/api/delete-user`, {
        method: 'DELETE',  // Use the DELETE HTTP method
        headers: {
            'X-CSRFToken': csrfToken  // Include the CSRF token in the headers for security
        }
    })
    .then(response => {
        // Redirect the user to the home page after successful deletion
        window.location.href = '/';
    })
    .catch(error => console.error('Error:', error))  // Log any errors that occur during the request
    .finally(() => {
        // Hide the delete confirmation modal after the operation completes
        $('#deleteConfirmationModal').modal('hide');
    });
}

// Function to get a cookie value by its name
export function getCookie(name) {
    let cookieValue = null;  // Initialize the cookie value as null
    if (document.cookie && document.cookie !== '') {  // Check if cookies are present
        const cookies = document.cookie.split(';');  // Split the cookies string into individual cookies
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();  // Trim any whitespace from the cookie
            // Check if the cookie starts with the specified name followed by an '='
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                // Decode and assign the cookie value
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;  // Break out of the loop once the desired cookie is found
            }
        }
    }
    return cookieValue;  // Return the cookie value or null if not found
}
