from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    event = models.ForeignKey(Event, on_delete= models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.username} - {self.event.name}'
