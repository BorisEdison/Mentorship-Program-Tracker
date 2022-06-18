from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile,User
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Adminpage(request):
    user = User.objects.all()
    context = {'user': user} 
    return render(request, 'admin.html', context)

# def faculty(request):
#     user = User.objects.all()
#     context = {'user': user}
#     return render(request, 'faculty-dashboard.html', context)

@login_required
def student(request, pk):
    user = User.objects.get(usr_id=pk)
    student=StudentProfile.objects.get(user=user)
    context = {'student' : student}
    return render(request, 'student-dashboard.html', context)



# def stud_prof(request):
#     return render(request, 'student-profile.html')
