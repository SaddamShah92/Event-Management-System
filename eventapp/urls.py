from django.urls import path
from .views import register_for_event

urlpatterns = [
    path("register-event/", register_for_event, name="register_event"),
]
