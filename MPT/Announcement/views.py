from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from accounts.models import *
from django.shortcuts import render, redirect


@login_required(login_url='Login')
def facultyAnnouncement(request):
    return render(request, 'Announcement/faculty-announcement.html')

@login_required(login_url='Login')
def facultyAnnouncementNew(request):
    if request.method == 'POST':
        announcement = Announcement()
        announcement.sender = request.user
        announcement.title = request.POST['title']
        announcement.content = request.POST['content']
        announcement.save()
        year=request.POST['inlineRadioOptions']
        
        try: 
            AnnouncementReceiver.objects.create(announcement=announcement, receiver=request.user).save()
            if year != 'ALL':
                for mentee in Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id ,Mentee__studentdetails__current_year=year):
                    AnnouncementReceiver.objects.create(receiver=mentee.Mentee.user, announcement=announcement).save()
            else:
                for mentee in Mentor_assign.objects.filter(Mentor__user=request.user):
                    AnnouncementReceiver.objects.create(receiver=mentee.Mentee.user, announcement=announcement).save()
        except:
            pass
        return redirect('faculty-announcement')

            
    return render(request, 'Announcement/faculty-announcement-new.html')


def studentAnnouncement(request):
    return render(request, 'Announcement/student-announcement.html')


@login_required(login_url='Login')
def deleteAnnouncement(request, id):
    notification = Announcement.objects.get(id=id)
    notification.delete()
    return redirect('faculty-announcement')
