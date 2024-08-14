// Check if the browser supports the replaceState method
if (window.history.replaceState) {
    // Replace the current history state with a new one to prevent form resubmission
    window.history.replaceState(null, null, window.location.href);
}
