from django.urls import path
from .views import contact_coach

urlpatterns = [
    path('', contact_coach, name='contact_coach'),
]