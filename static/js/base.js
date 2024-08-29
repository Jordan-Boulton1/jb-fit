// Check if the browser supports the replaceState method
if (window.history.replaceState) {
    // Replace the current history state with a new one to prevent form resubmission
    window.history.replaceState(null, null, window.location.href);
}

document.addEventListener('DOMContentLoaded', function () {
    var successMessageCloseBtns = document.getElementsByClassName("closesuccessbtn");
    closeParentElement(successMessageCloseBtns);

    var warningMessageCloseBtns = document.getElementsByClassName("closebtn");
    closeParentElement(warningMessageCloseBtns);

    var errorMessageCloseBtn = document.getElementsByClassName('closeerrorbtn');
    closeClosestParentElementOnError(errorMessageCloseBtn);
   
});


function closeParentElement(btns) {
    Array.from(btns).forEach(element => {
        element.addEventListener('click', function () {
            element.parentElement.style.display = 'none';
        });
    });
}

function closeClosestParentElementOnError(btns) {
    Array.from(btns).forEach(element => {
        element.addEventListener('click', function () {
            var parent = this.closest('.alert'); // Find the closest parent with class 'alert'
            if (parent) {
                parent.style.display = 'none'; // Hide the parent element
            }
        });
    });
}