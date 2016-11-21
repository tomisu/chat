from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room)
    user = models.CharField(max_length=32)
    date = models.DateTimeField(default = timezone.now)
    message = models.TextField()

    def __str__(self):
        return "{} in {}, at {} - {}".format(self,user, self.room, self.date, self.message[0:10])
