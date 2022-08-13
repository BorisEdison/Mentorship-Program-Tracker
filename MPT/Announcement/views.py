from django.shortcuts import render

def facultyAnnouncement(request):
    return render(request, 'Announcement/faculty-announcement.html' )

def studentAnnouncement(request):
    return render(request, 'Announcement/student-announcement.html' )