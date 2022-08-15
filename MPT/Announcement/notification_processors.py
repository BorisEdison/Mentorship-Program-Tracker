from .models import *

def announcements(request):
    allnotifications= Announcement.objects.all()
    return {'notifications':allnotifications}

def announcement_receiver(request):
    allreceivers= AnnouncementReceiver.objects.all()
    return {'receivers':allreceivers}