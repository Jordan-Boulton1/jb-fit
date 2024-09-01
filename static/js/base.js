/* jshint esversion: 11, jquery: true */
/* global bootstrap */

// Prevent form resubmission on page reload
if (window.history.replaceState) {
    // Replace the current history state with the same URL to prevent form resubmission
    window.history.replaceState(null, null, window.location.href);
}

// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Add click event listeners to all close buttons of various types
    setupCloseButtons('.closebtn-variant');  // Close buttons with '.closebtn-variant' class
    setupCloseButtons('.closebtn');          // Close buttons with '.closebtn' class
    setupCloseButtons('.closeerrorbtn');     // Close buttons with '.closeerrorbtn' class

    // Initialize Bootstrap tooltips
    loadTooltips();
});

/**
 * Sets up click event listeners on buttons with the specified selector
 * to close their parent alert elements.
 * 
 * @param {string} selector - The CSS selector for the close buttons.
 */
export function setupCloseButtons(selector) {
    // Select all elements matching the selector
    var closeBtns = document.querySelectorAll(selector);
    closeBtns.forEach(function (btn) {
        // Add a click event listener to each button
        btn.addEventListener('click', function () {
            var parentAlert = this.closest('.alert'); // Find the closest '.alert' parent element
            if (parentAlert) {
                parentAlert.style.display = 'none'; // Hide the alert when the button is clicked
            }
        });
    });
}

/**
 * Initializes Bootstrap tooltips on elements with the data-bs-toggle attribute set to 'tooltip'.
 */
export function loadTooltips() {
    // Convert NodeList of tooltip trigger elements into an array
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    // Initialize a Bootstrap tooltip on each element in the array
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);  // Create a new tooltip instance for each element
    });
}
