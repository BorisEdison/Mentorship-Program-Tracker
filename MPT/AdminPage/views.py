from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# student dashboard view
@login_required
def student(request, pk):
    if request.user.is_authenticated and not(request.user.is_staff):
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

# Create your views here for admin page

@login_required
def Adminpage(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {'users': users} 
        return render(request,'AdminPage/admin-user.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

# view all the students in the database in the admin page
@login_required
def Adminstudent(request):
    if request.user.is_superuser:
        students = StudentProfile.objects.all()
        context = {'students': students} 
        return render(request,'AdminPage/admin-student.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Adminmentor(request):
    if request.user.is_superuser:
        mentors = MentorProfile.objects.all()
        context = {'mentors': mentors} 
        return render(request,'AdminPage/admin-mentor.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Activity(request):
    if request.user.is_superuser:
        return render(request,'AdminPage/admin-activities.html')
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def deleteuser(request,id):
    if request.user.is_superuser:
        if request.method=='POST':
            # User.objects.filter(pk=id).delete()
            user=User.objects.get(pk=id)
            check=user.is_staff
            user.delete()
            if check:
                return redirect('admin-mentor')
            else:
                return redirect('admin-student')

    return HttpResponse("You are not authorized to view this page")