from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import *
from FacultyDashboard.models import *
from django.contrib.auth.decorators import login_required
import datetime
from Announcement.models import *


from Marks.models import AcademicScores

# Create your views here.
@login_required(login_url='Login')
def student(request, pk):

    tp = User.objects.get(usr_id=pk)
    stu= get_object_or_404(StudentProfile, user = tp)    
    qs = AcademicScores.objects.filter(student = stu).order_by('academicYear','sem','sub_code','exam')
    distinct_sem_yr = AcademicScores.objects.all().values('academicYear','sem').distinct()
    distinct_yr = AcademicScores.objects.all().values('academicYear').distinct()
    distinct_sem = AcademicScores.objects.all().values('sem').distinct()

    chartdict={}
    for i in distinct_yr:
        chartdict[i['academicYear']]=AcademicScores.objects.filter(academicYear=i['academicYear']).values('sem').distinct()
    
    if request.user.is_authenticated and not(request.user.is_staff):
        user = User.objects.get(usr_id=pk)
        student=StudentProfile.objects.get(user=user)
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
        unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
        context={'user':user,
                'student':student,
                'unread_announcement':unread_announcements,
                'unseen_meetings':unseen_meetings,
                'qs':qs,
                'distinct_sem_yr':distinct_sem_yr,
                'distinct_yr':distinct_yr,
                'distinct_sem':distinct_sem
                }
        if student.is_assigned:
            try:
                obj=Mentor_assign.objects.get(Mentee__user__usr_id=pk)
                mentor=User.objects.get(email=obj.Mentor)
                context['mentor']= mentor.first_name+' '+mentor.last_name
            except:
                pass
        try:
            details=StudentDetails.objects.get(student_id=student.id)
            hobbies=StudentHobbies.objects.get(student_id=student.id)
            guardian=GuardianDetails.objects.get(student_id=student.id)
            Medical=StudentMedicalReport.objects.get(student_id=student.id)
            extraCurr=StudentExtraCurricular.objects.get(student_id=student.id)
            achievements=[i for i in extraCurr.achievements.split(',')]
            clubs=[i for i in extraCurr.clubs.split(',')]
            hobbies=[i for i in hobbies.hobby.split(',')]
            organizations=[i for i in extraCurr.organization.split(',')]
            context.update({'student' : student,'details':details,'hobbies':hobbies,'guardian':guardian,'clubs':clubs,'hobbies':hobbies,'achievements':achievements,'orgs':organizations,'Medical':Medical})
        except:
            pass
        return render(request, 'student-dashboard.html', context)

@login_required(login_url='Login')
def studentMeeting(request):
    student=StudentProfile.objects.get(user__usr_id=request.user.usr_id)
    Meeting.objects.filter(Receiver=student, is_read=False).update(is_read=True)
    return render(request, 'student-meeting.html')

def studentMeetingRecords(request):
    student=StudentProfile.objects.get(user__usr_id=request.user.usr_id)
    meetings=Meeting.objects.filter(Receiver=student)
    context={
        'student':student,
        'meetingrecords':meetings,
        'todays_date':datetime.date.today(),
        'current_time':datetime.datetime.now().time()
    }
    return render(request, 'student-meeting-records.html',context)