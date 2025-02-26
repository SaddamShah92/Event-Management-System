from django import forms
from . models import Event

class EventForm(forms.ModelForm):
    class Meta:
     model = Event
     fields = ['name', 'date_time', 'description', 'location']
     widgets = {
        'date_time' : forms.DateTimeInput(attrs={'type' : 'datetime-local'}),
    }