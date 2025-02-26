from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all().order_by('date_time')
    return render(request, 'event_list.html', {'events' : events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to event list after adding
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})



