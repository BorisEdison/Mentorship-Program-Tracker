from django.shortcuts import render

def announcement(request):
    return render(request, 'Announcement/faculty-announcement.html' )