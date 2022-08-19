from django.db import models
from accounts.models import *

class Meeting(models.Model):
    Meeting_id = models.AutoField(primary_key=True)
    Sender = models.ForeignKey(MentorProfile, on_delete=models.CASCADE, related_name='sender')
    Receiver = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='receiver')
    Meeting_title = models.CharField(max_length=100)
    Meeting_description = models.TextField(null=True)
    Meeting_date = models.DateField(null=True)
    Meeting_time = models.TimeField(null=True)
    Meeting_link = models.URLField(null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Meeting_title + ' - ' + self.Sender.user.first_name + ' - ' + self.Receiver.user.first_name

    class Meta:
        ordering = ('Meeting_date','Meeting_time')
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'

class MeetingAttendance(models.Model):
    Meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    Attendance = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Meeting_id.Meeting_title + ' - ' + self.Student.user.first_name + ' - ' + self.Attendance

    class Meta:
        ordering = ('Meeting_id','created_at')
        verbose_name = 'Meeting Attendance'
        verbose_name_plural = 'Meetings Attendance'
