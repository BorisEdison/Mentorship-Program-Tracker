from django.shortcuts import render
from accounts.models import *
from FacultyDashboard.models import *
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='Login')
def student(request, pk):
    if request.user.is_authenticated and not(request.user.is_staff):
        user = User.objects.get(usr_id=pk)
        student=StudentProfile.objects.get(user=user)
        context={'user':user,'student':student} 
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