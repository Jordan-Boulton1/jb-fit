from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.profile_view, name='profile'),
    path("accounts/profile/edit/", views.edit_profile_view, name='edit_profile'),
    path('add_weight_log/', views.add_weight_log, name='add_weight_log'),
    path("api/weight-logs-chart/", views.get_user_weight_logs, name='get_user_weight_logs'),
    path("api/weight-logs-history/", views.get_user_weight_logs_history, name='get_user_weight_logs_history'),
    path('edit-weight-log/<int:log_id>/', views.edit_weight_log, name='edit_weight_log'),
    path('api/delete-weight-log/<int:log_id>/', views.delete_weight_log, name='delete-weight-log'),
]
