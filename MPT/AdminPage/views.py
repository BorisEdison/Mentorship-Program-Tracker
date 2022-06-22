from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Adminpage(request):
    if request.user.is_superuser:
        user = User.objects.all()
        context = {'user': user} 
        return render(request,'AdminPage/admin-user.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def student(request, pk):
    user = User.objects.get(usr_id=pk)
    student=StudentProfile.objects.get(user=user)
    context={'user':user,'student':student} 
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
        context = {'student' : student,'details':details,'hobbies':hobbies,'guardian':guardian,'clubs':clubs,'hobbies':hobbies,'achievements':achievements,'orgs':organizations,'Medical':Medical}
    except:
        pass
    return render(request, 'student-dashboard.html', context)
