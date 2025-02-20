from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    registered_users = models.ManyToManyField(User, related_name= "registered_events", blank=True)

    def __str__(self):
        return self.name
