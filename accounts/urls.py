from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.profile_view, name='profile'),
    path("accounts/profile/edit/", views.edit_profile_view, name='edit_profile'),
]
