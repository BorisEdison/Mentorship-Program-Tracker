from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from FacultyDashboard.models import *
from accounts.models import *
from django.core.mail import send_mail
from MPT import settings    
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import Http404

@staff_member_required(login_url='login')
def facultyAnnouncement(request):
    AnnouncementReceiver.objects.filter(receiver=request.user, is_read=False).update(is_read=True)
    return render(request, 'Announcement/faculty-announcement.html')

@staff_member_required(login_url='Login')
def facultyAnnouncementNew(request):
    if request.method == 'POST':
        announcement = Announcement()
        sender = request.user
        title = request.POST['title']
        content = request.POST['content']
        announcement.sender = sender
        announcement.title = title
        announcement.content = content
        announcement.save()
        year=request.POST['inlineRadioOptions']
        
        try: 
            AnnouncementReceiver.objects.create(announcement=announcement, receiver=request.user).save()
            if year != 'ALL':
                for mentee in Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id ,Mentee__studentdetails__current_year=year):
                    AnnouncementReceiver.objects.create(receiver=mentee.Mentee.user, announcement=announcement).save()
                    mail_subject= str(title)
                    message= render_to_string('Announcement/announcement_email.html', {
                        'sender': str(sender.first_name) + ' ' + str(sender.last_name),
                        'receiver': str(mentee.Mentee.user.first_name) + ' ' + str(mentee.Mentee.user.last_name),
                        'announcement':content,
                        'title': title,
                    })
                    to_email= mentee.Mentee.user.email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                    except:
                        print('Error Occured In Sending Mail, Try Again ')
                        pass
            else:
                for mentee in Mentor_assign.objects.filter(Mentor__user=request.user):
                    AnnouncementReceiver.objects.create(receiver=mentee.Mentee.user, announcement=announcement).save()
                    mail_subject= str(title)
                    message= render_to_string('Announcement/announcement_email.html', {
                        'sender': str(sender.first_name) + ' ' + str(sender.last_name),
                        'receiver': str(mentee.Mentee.user.first_name) + ' ' + str(mentee.Mentee.user.last_name),
                        'announcement':content,
                        'title': title,
                    })
                    to_email= mentee.Mentee.user.email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                    except:
                        print('Error Occured In Sending Mail, Try Again ')
                        pass
        except:
            pass
        return redirect('faculty-announcement')

    return render(request, 'Announcement/faculty-announcement-new.html')


@staff_member_required(login_url='Login')
def deleteAnnouncement(request, id):
    notification = Announcement.objects.get(id=id)
    notification.delete()
    return redirect('faculty-announcement')

@login_required(login_url='Login')
def studentAnnouncement(request):
    if not request.user.is_staff:
        AnnouncementReceiver.objects.filter(receiver=request.user, is_read=False).update(is_read=True)
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
        student = get_object_or_404(StudentProfile, user = request.user)    
        unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
        return render(request, 'Announcement/student-announcement.html',{'unread_announcements':unread_announcements,'unseen_meetings':unseen_meetings})
    else:
        raise Http404("You are not allowed to access this page")
