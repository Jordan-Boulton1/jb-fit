document.addEventListener('DOMContentLoaded', function () {
    // Set up the click event for the confirm delete button
    $('#promptConfirmDelete').on('click', () => {
        showConfirmationModal();
    });
    $('#confirmDeleteButton').on('click', () => {
        deleteUserAccount();
    });
});


function showConfirmationModal() {
    var confirmationModal = document.getElementById('deleteConfirmationModal');
    var modal = new bootstrap.Modal(confirmationModal);
    modal.show();
}


function deleteUserAccount(){
    const csrfToken = getCookie('csrftoken');
    fetch(`/api/delete-user`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        window.location.href = '/';
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        $('#deleteConfirmationModal').modal('hide');
    });
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