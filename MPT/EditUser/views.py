from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile,User, MentorProfile


# need to do 1-1 relationship with user and mentor while registration 
@login_required
def edit(request):
    context={}
    # print(request.user)
    # print(request.user.id)
    if request.user.is_staff:
            profile = MentorProfile.objects.get(user__id=request.user.id)
            print("mentor id",profile.id)
            print("user id",profile.user.id)

            print(profile.Branch)

            context={   'profile': profile,
                        'id': request.user.id}

            if request.method=="POST":
                print("user id after post",profile.user.id)
                print("mentor id after post",profile.id)

                fName = request.POST['fName']
                Lname= request.POST['lName']
                department= request.POST['dept']
                motherTongue= request.POST['mTongue']
                religion= request.POST['Religion']
                # phone= request.POST['phone']
                # email= request.POST['email']
                # email1= request.POST['email1']
                # password1= request.POST['password1']
                # password2= request.POST['password2']
                city = request.POST['city']
                profile_img= request.FILES['profileImg']
                user = User.objects.get(id=request.user.id)
                if str(user.profile_img) != 'logo.png': # if user already has profile image then delete it
                    user.profile_img.delete()
                user.first_name= fName
                user.profile_img=profile_img
                user.last_name=Lname
                user.save()

                profile.city = city
                profile.Branch = department
                profile.mother_tongue = motherTongue
                profile.religion = religion
                # print(profile.city)
                profile.save()
                # print("hello1")
                return redirect('faculty', pk = user.id)
            else:
                return render(request,'faculty-edit.html', context)

    else:
        profile = StudentProfile.objects.get(user__id=request.user.id)
        context={'profile': profile}
        print(request.user)
        if request.method=="POST":
            fName = request.POST['fName']
            Lname = request.POST['LName']
            department = request.POST['department']
            # phone= request.POST['phone']
            # email= request.POST['email']
            # email1= request.POST['email1']
            # password1= request.POST['password1']
            # password2= request.POST['password2']
            profile_img= request.FILES['profile_img']
            user = User.objects.get(id=request.user.id)
            if str(user.profile_img) != 'logo.png': # if user already has profile image then delete it
                user.profile_img.delete()
            user.first_name= fName
            user.last_name=Lname
            user.profile_img=profile_img
            user.save()

            profile.department= department
            profile.save()
            
            return redirect('/studentdashboard')


        else:
            return render(request,'edit-student-details.html', context)