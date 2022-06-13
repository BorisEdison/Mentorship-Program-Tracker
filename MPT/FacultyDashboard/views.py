from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile,MentorProfile,Mentor_assign
from django.contrib.auth.decorators import permission_required
from accounts.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required





# Create your views here.
def studentdetail(request, pk):
    user = User.objects.get(id=pk)
    context = {'users': user}
    return render(request, 'student-profile.html', context)


def faculty(request,pk):
    # current_user = request.user
    # user_id = current_user.id
    # print(user_id)
    students = Mentor_assign.objects.filter(Mentor__id = pk )
    # students = mentee.StudentProfile_set.all()


    user = User.objects.all()  
    context = {'user': user, 'students': students}
    return render(request, 'faculty-dashboard.html', context)