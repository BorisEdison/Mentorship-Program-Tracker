from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile


# need to do 1-1 relationship with user and mentor while registration
@login_required
def edit(request):
    context = {}
    if request.user.is_staff:
        profile = MentorProfile.objects.get(user__usr_id=request.user.usr_id)

        # print("mentor id", profile.id)
        # print("user id", profile.user.id)
        # print(profile.Branch)

        context = {
            'department_list': [
                'Computer Engineering',
                'Electronics and Telecommunication Engineering',
                'Information Technology',
                'Mechanical Engineering'
            ],
            'bloodGroup_list': [
                'A+',
                'A-',
                'B+',
                'B-',
                'AB+',
                'AB-',
                'O+',
                'O-'
            ],
            'profile': profile,
            'id': request.user.usr_id
        }

        if request.method == "POST":
            print("user id after post", profile.user.usr_id)
            print("mentor id after post", profile.id)

            fName = request.POST['fName']
            Lname = request.POST['lName']
            Mname = request.POST['mName']
            motherTongue = request.POST['mTongue']
            religion = request.POST['Religion']
            phone = request.POST['phone']
            State = request.POST['state']
            Country = request.POST['country']
            Addr = request.POST['Address']
            Qualification = request.POST['Quali']
            Teacherid = request.POST['usr_id']
            city= request.POST['city']
            try:
                if request.POST['dept'] :
                    department = request.POST['dept']
                    profile.Branch = department
            except:
                pass
            try:
                if request.POST['blood_group']:
                    blood_group = request.POST['blood_group']
                    profile.Blood_grp = blood_group
            except:
                pass
            try:
                if request.POST['gender']:
                    gender = request.POST['gender']
                    profile.Gender = gender
            except:
                pass
            try:
                if request.POST['dob']:
                    DateofBirth = request.POST['dob']
                    profile.DateofBirth = DateofBirth
            except:
                pass

            try:
                if request.POST['doj']:
                    DateofJoining= request.POST['doj']
                    profile.DateofJoining = DateofJoining
            except:
                pass

            user = User.objects.get(usr_id=request.user.usr_id)
            try:
                if 'profileImg' in request.FILES:
                    profile_img = request.FILES['profileImg']
                    # if user already has profile image then delete it
                    if str(user.profile_img) != 'logo.png':
                        user.profile_img.delete()
                    user.profile_img = profile_img
            except:
                pass
        
            user.first_name = fName
            user.usr_id= Teacherid
            user.middle_name=Mname
            user.last_name = Lname
            user.phone = phone
            user.save()
            
            profile.City = city
            profile.qualification= Qualification
            profile.State = State
            profile.Address= Addr
            profile.Country= Country
            profile.mother_tongue = motherTongue
            profile.religion = religion
            profile.save()
            return redirect('faculty', pk=user.usr_id)
        else:
            return render(request, 'EditUser/faculty-edit.html', context)

    else:
        profile = StudentProfile.objects.get(user__usr_id=request.user.usr_id)
        context = {
            'department_list': [
                'Computer Engineering',
                'Electronics and Telecommunication Engineering',
                'Information Technology',
                'Mechanical Engineering'
            ],
            'bloodGroup_list': [
                'A+',
                'A-',
                'B+',
                'B-',
                'AB+',
                'AB-',
                'O+',
                'O-'
            ],
            'profile': profile,
            'pk': request.user.usr_id
        }
        if request.method == "POST":
            fName = request.POST['fName']
            Lname = request.POST['lName']
            Mname = request.POST['mName']
            stuid = request.POST['sId']
            Addr = request.POST['Address']
            religion = request.POST['Religion']
            motherTongue = request.POST['mTongue']
            phone = request.POST['phone']
            try:
                if request.POST['dept'] :
                    department = request.POST['dept']
                    profile.Branch = department
            except:
                pass
            try:
                if request.POST['blood_group']:
                    blood_group = request.POST['blood_group']
                    profile.Blood_grp = blood_group
            except:
                pass
            try:
                if request.POST['gender']:
                    gender = request.POST['gender']
                    profile.Gender = gender
            except:
                pass
            try:
                if request.POST['dob']:
                    DateofBirth = request.POST['dob']
                    profile.DateofBirth = DateofBirth
            except:
                pass

            
            user = User.objects.get(usr_id=request.user.usr_id)
            try:
                if 'profileImg' in request.FILES:
                    profile_img = request.FILES['profileImg']
                    # if user already has profile image then delete it
                    if str(user.profile_img) != 'logo.png':
                        user.profile_img.delete()
                    user.profile_img = profile_img
            except:
                pass
            user.first_name = fName
            user.usr_id= stuid
            user.middle_name=Mname
            user.last_name = Lname
            user.phone = phone
            user.save()

            profile.Address= Addr
            profile.religion = religion
            profile.mother_tongue = motherTongue
            profile.save()
            return redirect('student',pk=user.usr_id)

        else:
            return render(request, 'student-edit.html', context)
