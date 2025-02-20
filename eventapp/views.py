from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventRegistrationForm

@login_required
def register_for_event(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data["event"]
            event.registered_users.add(request.user)  # Add the user to the event
            return redirect("event_list")  # Redirect to event list page
    else:
        form = EventRegistrationForm()

    return render(request, "event_registration.html", {"form": form})
