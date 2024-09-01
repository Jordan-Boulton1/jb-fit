from django.urls import path, include
from . import views

# Define URL patterns for the application
urlpatterns = [
    # Include the default Django authentication URLs
    # (login, logout, password management)
    path("accounts/", include("django.contrib.auth.urls")),

    # URL pattern for the user's profile page.
    path(
        "accounts/profile/",
        views.profile_view,
        name='profile'  # Name used to refer to this URL in templates and views
    ),

    # URL pattern for viewing the user's order history.
    path(
        "accounts/profile/user_order_history",
        views.user_order_history,
        name='user_order_history'
    ),

    # URL pattern for the page where users can edit their profile information.
    path(
        "accounts/profile/edit/",
        views.edit_profile_view,
        name='edit_profile'
    ),

    # URL pattern for adding a new weight log entry.
    path(
        'add_weight_log/',
        views.add_weight_log,
        name='add_weight_log'
    ),

    # URL pattern for uploading progress pictures.
    path(
        'upload-progress-picture/',
        views.upload_progress_picture,
        name='upload_progress_picture'
    ),

    # URL pattern for deleting a specific progress picture by its ID.
    path(
        'delete_progress_picture/<int:picture_id>/',
        views.delete_progress_picture,
        name='delete_progress_picture'
    ),

    # API URL pattern for fetching user weight logs for chart display.
    path(
        "api/weight-logs-chart/",
        views.get_user_weight_logs,
        name='get_user_weight_logs'
    ),

    # API URL pattern for fetching the user's weight logs history.
    path(
        "api/weight-logs-history/",
        views.get_user_weight_logs_history,
        name='get_user_weight_logs_history'
    ),

    # URL pattern for editing a specific weight log entry by its ID.
    path(
        'edit-weight-log/<int:log_id>/',
        views.edit_weight_log,
        name='edit_weight_log'
    ),

    # API URL pattern for deleting a specific weight log entry by its ID.
    path(
        'api/delete-weight-log/<int:log_id>/',
        views.delete_weight_log,
        name='delete-weight-log'
    ),

    # API URL pattern for deleting the user's profile.
    path(
        'api/delete-user/',
        views.delete_user_profile,
        name='delete-user'
    ),
]
