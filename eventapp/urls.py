from django.urls import path
from .views import event_list, add_event

urlpatterns = [
    path("", event_list, name="event_list"),
    path('add/' , add_event, name = 'add_event'),
]
