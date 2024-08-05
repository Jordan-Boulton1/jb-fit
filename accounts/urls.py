from django.urls import path, include
from .views import profile_view

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", profile_view, name='profile')
]
