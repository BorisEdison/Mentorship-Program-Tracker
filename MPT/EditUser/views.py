from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile
from accounts.models import User


#  need to do 1-1 relationship with user and mentor while registration 
def edit(request):
    context={}
    if request.user.is_staff:
            # profile = MentorProfile.objects.get(user__id=request.user.id)
            if request.method=="POST":
                fName = request.POST['fName']
                Lname= request.POST['LName']
                username= request.POST['username']
                department= request.POST['department']
                # phone= request.POST['phone']
                # email= request.POST['email']
                # email1= request.POST['email1']
                # password1= request.POST['password1']
                # password2= request.POST['password2']
                user = User.objects.get(id=request.user.id)
                user.first_name= fName
                user.username=username
                user.last_name=Lname
                user.save()

                # profile.Branch = department
                # profile.save()
                # context={'profile': profile}
                return redirect('/facultydashboard')
            else:
                return render(request,'edit.html', context)

    else:
        profile = StudentProfile.objects.get(user__id=request.user.id)
        print(request.user)
        if request.method=="POST":
            fName = request.POST['fName']
            Lname = request.POST['LName']
            username = request.POST['username']
            department = request.POST['department']
            # phone= request.POST['phone']
            # email= request.POST['email']
            # email1= request.POST['email1']
            # password1= request.POST['password1']
            # password2= request.POST['password2']
            user = User.objects.get(id=request.user.id)
            user.first_name= fName
            user.username=username
            user.last_name=Lname
            user.save()

            profile.department= department
            profile.save()
            context={'profile': profile}
            return redirect('/studentdashboard')


        else:
            return render(request,'edit.html', context)