// Prevent form resubmission on page reload
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

document.addEventListener('DOMContentLoaded', function () {
    // Add click event listeners to all close buttons
    setupCloseButtons('.closebtn-variant');
    setupCloseButtons('.closebtn');
    setupCloseButtons('.closeerrorbtn');

    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

/**
 * Sets up click event listeners on buttons with the specified selector
 * to close their parent alert elements.
 * 
 * @param {string} selector - The CSS selector for the close buttons.
 */
function setupCloseButtons(selector) {
    // Select all elements matching the selector
    var closeBtns = document.querySelectorAll(selector);
    closeBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var parentAlert = this.closest('.alert'); // Find the closest '.alert' parent
            if (parentAlert) {
                parentAlert.style.display = 'none'; // Hide the alert
            }
        });
    });
}
