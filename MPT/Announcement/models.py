from django.db import models
from accounts.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Announcement(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField('date published', auto_now_add=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class AnnouncementReceiver(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE,null=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['announcement']

    def __str__(self):
        return 'Title: {} is sended by {} to {}.'.format(self.announcement.title, self.announcement.sender, self.receiver)
