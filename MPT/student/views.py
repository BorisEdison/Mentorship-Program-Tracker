from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import *
from FacultyDashboard.models import *
from django.contrib.auth.decorators import login_required
from Announcement.models import *
from Marks.models import *
import datetime

@login_required(login_url='Login')
def student(request, pk):
    
    if request.user.is_authenticated and not(request.user.is_staff):
        user = User.objects.get(usr_id=pk)
        student=StudentProfile.objects.get(user=user)
        cgpa,created=SemCGPA.objects.get_or_create(student=student)
        cgpa_dict={}
        try:
            for i in ['I','II','III','IV','V','VI','VII','VIII']:
                cgpa_dict['SEMESTER '+i] = cgpa.__dict__['sem'+i]
        except:
            pass
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
        unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
        distinct_sem_yr = AcademicScores.objects.filter(student=student).values('academicYear','sem','exam').distinct().order_by('academicYear','sem','sub_code','exam')
        chartdict={}
        for i in distinct_sem_yr:
            distinct_subs=AcademicScores.objects.filter(academicYear=i['academicYear'],sem=i['sem']).values('sub_code').distinct()
            sub_code_dict={}
            for j in distinct_subs:
                sub_code_dict[j['sub_code']]=AcademicScores.objects.filter(academicYear=i['academicYear'],sem=i['sem'],sub_code=j['sub_code']).values('exam','marks')
            chartdict[str(i['academicYear'])+" SEMESTER " +str(i['sem'])]=sub_code_dict

        context={'user':user,
                'student':student,
                'unread_announcement':unread_announcements,
                'unseen_meetings':unseen_meetings,
                'chartdict':chartdict,
                'cgpa_dict':cgpa_dict
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
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = request.user)    
    unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
    # student=StudentProfile.objects.get(user__usr_id=request.user.usr_id)
    Meeting.objects.filter(Receiver=student, is_read=False).update(is_read=True)
    return render(request, 'student-meeting.html',{'unread_announcement':unread_announcements,'unseen_meetings':unseen_meetings})

def studentMeetingRecords(request):
    # student=StudentProfile.objects.get(user__usr_id=request.user.usr_id)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = request.user)    
    unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()

    meetings=Meeting.objects.filter(Receiver=student)
    context={
        'student':student,
        'meetingrecords':meetings,
        'todays_date':datetime.date.today(),
        'current_time':datetime.datetime.now().time(),
        'unread_announcement':unread_announcements,
        'unseen_meetings':unseen_meetings
    }
    return render(request, 'student-meeting-records.html',context)