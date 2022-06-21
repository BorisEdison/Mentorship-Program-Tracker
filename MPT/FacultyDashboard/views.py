from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm

from accounts.models import StudentProfile, StudentDetails, MentorProfile, Mentor_assign
from django.contrib.auth.decorators import permission_required
from accounts.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


#logout the logged in user
def logout(request):
    django_logout(request)
    return redirect('/')

# Create your views here.
@login_required
def studentdetail(request, fac_id, stu_id):
    user = User.objects.get(usr_id=stu_id)
    faculty = User.objects.get(usr_id=fac_id)
    # user = StudentDetails.objects.get(student__user__usr_id = request.user.usr_id)
    # user = User.objects.get(usr_id=pk)
    # print (request.user.usr_id)
    # print(user.usr_id)
    studentProfile = StudentProfile.objects.get(user__usr_id = stu_id)
    # print(studentProfile.user.usr_id)
    # details = StudentDetails.objects.get(student__usr_id = studentProfile.user.usr_id)
    
               
    context =  { 'user': user,
                'faculty':faculty,  
                'StudentProfile': studentProfile
                # 'StudentDetail': details
                }
    return render(request, 'FacultyDashboard/faculty-student-profile.html', context)

@login_required
def faculty(request,pk):
    if request.user.is_staff:
        ## current_user = request.user
        # user_id = current_user.id
        # print(user_id)
        print(request.user.usr_id)
        # mentor = MentorProfile.objects.get(user__usr_id=pk)
        students = Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id)
        #students = Mentor_assign.objects.filter(Mentor__id = pk )
        # students = mentee.StudentProfile_set.all()
        # print(mentor.id)
    
        #print(students)
        # user = User.objects.all()  
        context = { 'students': students,
                    'fac_id': pk}
                    # 'mentor': mentor
                    
        return render(request, 'FacultyDashboard/faculty-dashboard.html', context)

    else:
        return HttpResponse("You are not authorized to view this page")    