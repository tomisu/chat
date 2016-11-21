from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=64)

    def send_message(self, user, content):
        new_message = Message()
        new_message.room = self
        new_message.user = user
        new_message.content = content
        new_message.save()

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages")
    user = models.CharField(max_length=32)
    date = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return "{} in {}, at {} - {}".format(self.user, self.room, self.date, self.content[0:10])
