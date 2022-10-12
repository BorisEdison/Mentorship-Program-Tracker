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
from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
from Announcement.models import *
from FacultyDashboard.models import *
import phonenumbers

studentcontext={
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
            'year_list': [
                'FE',
                'SE',
                'TE',
                'BE',
                'Graduated',
            ],
            'qualification_list': [
                'No formal education',
                'Primary education',
                'Secondary education',
                'Higher secondary education',
                'GED: Diploma',
                'Vocational qualification',
                'Bachelor\'s degree',
                'Master\'s degree',
                'Doctorate or higher degree'
            ],
            'occupation_list': [
                'Healthcare Practitioners and Technical Occupation',
                'Healthcare Support Worker',
                'Business, Executive, Management, and Financial Occupation',
                'Architecture and Engineering Occupation',
                'Education, Training, and Library Occupation',
                'Other Professional Occupation',
                'Office and Administrative Support Occupation',
                'Services Occupation',
                'Agriculture, Maintenance, Repair, and Skilled Crafts Occupation',
                'Transportation Occupations and Craft Operator',
                'Other Occupation'
            ],
            
        }
# need to do 1-1 relationship with user and mentor while registration
@login_required(login_url='Login')
def edit(request):
    context = {}
    if request.user.is_staff:
        profile = MentorProfile.objects.get(user__usr_id=request.user.usr_id)
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()

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
            'id': request.user.usr_id,
            'unread_announcement':unread_announcements,
        }

        if request.method == "POST":
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
            # try:
            #     if request.POST['link'] :
            #         meet_link = request.POST['link']
            #         print('this is meet link',meet_link)
            #         profile.meeting_link = meet_link
            # except:
            #     pass
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
        
            if phonenumbers.is_valid_number(phonenumbers.parse(phone, "IN")):
                user.phone = phone
            user.first_name = fName
            user.usr_id= Teacherid
            user.middle_name=Mname
            user.last_name = Lname
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

    elif request.user.is_staff == False:
        profile = StudentProfile.objects.get(user__usr_id=request.user.usr_id)
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
        unseen_meetings=Meeting.objects.filter(Receiver=profile,is_read=False).count()

        details,created=StudentDetails.objects.get_or_create(student_id=profile.id)
        hobbies,created=StudentHobbies.objects.get_or_create(student_id=profile.id)
        guardian,created=GuardianDetails.objects.get_or_create(student_id=profile.id)
        extraCurr,created=StudentExtraCurricular.objects.get_or_create(student_id=profile.id)
        Medical,created=StudentMedicalReport.objects.get_or_create(student_id=profile.id)
        context={
            'student': profile,
            'pk': request.user.usr_id,
            'details':details,
            'hobbies':hobbies,
            'guardian':guardian,
            'extraCurr':extraCurr,
            'Medical':Medical,
            'unread_announcement':unread_announcements,
            'unseen_meetings':unseen_meetings,
            }
        context.update(studentcontext)
        if request.method == "POST":
            fName = request.POST['fName']
            Lname = request.POST['lName']
            Mname = request.POST['mName']
            # stuid = request.POST['sId']
            Addr = request.POST['Address']
            religion = request.POST['Religion']
            motherTongue = request.POST['mTongue']
            phone = request.POST['phone']
            try:
                if request.POST['rNo'] :
                    Rno=request.POST['rNo']
                    details.current_rollNo=Rno
            except:
                pass
            try:
                if request.POST['dept'] :
                    department = request.POST['dept']
                    profile.Branch = department
            except:
                pass
            try:
                if request.POST['year'] :
                    year = request.POST['year']
                    details.current_year = year
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
                if request.POST['Yoa']:
                    yearOfAdd = request.POST['Yoa']
                    details.YearOfAdmission = yearOfAdd
            except:
                pass

            # guardian info
            FatherName = request.POST['FatherName']
            MotherName = request.POST['MotherName']
            try:
                if request.POST['Fqualification']:
                    Fqualif= request.POST['Fqualification']
                    guardian.fatherHighestEducation=Fqualif
            except:
                pass
            try:
                if request.POST['Mqualification']:
                    Mqualif= request.POST['Mqualification']
                    guardian.motherHighestEducation=Mqualif
            except:
                pass
            try:
                if request.POST['Foccup']:
                    Foccupation= request.POST['Foccup']
                    guardian.fatherOccupation=Foccupation
            except:
                pass
            try:
                if request.POST['Moccup']:
                    Moccupation= request.POST['Moccup']
                    guardian.motherOccupation=Moccupation
            except:
                pass
            try:
                if request.POST['income']:
                    income= request.POST['income']
                    guardian.yearlyIncome=income
            except:
                pass

            guardian.father_name=FatherName
            guardian.mother_name=MotherName

            # health info
            addiction= request.POST['addiction']
            illness= request.POST['illness']
            phobia= request.POST['phobia']
            treatment= request.POST['treatment']
            Medical.addiction=addiction
            Medical.illness=illness
            Medical.phobia=phobia
            Medical.treatment=treatment
            
            #Goals, Hobbies, Extra Curricular Activities
            aim= request.POST['aim']
            hobbie= request.POST['hobby']
            ReasonForEngg= request.POST['ReasonForEngg']
            Achievements= request.POST['achievements']
            clubs= request.POST['clubs']
            orgs= request.POST['orgs']

            details.reason_of_engg=ReasonForEngg
            details.AimOfLife=aim
            extraCurr.clubs=clubs
            extraCurr.achievements=Achievements
            extraCurr.organization=orgs
            hobbies.hobby=hobbie

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
            
            if phonenumbers.is_valid_number(phonenumbers.parse(phone, "IN")):
                user.phone = phone
            user.first_name = fName
            # user.usr_id= stuid
            user.middle_name=Mname
            user.last_name = Lname
            user.save()

            profile.Address= Addr
            profile.religion = religion
            profile.mother_tongue = motherTongue
            details.save()
            profile.save()
            guardian.save()
            hobbies.save()
            extraCurr.save()
            Medical.save()
            return redirect('student',pk=user.usr_id)

        else:
            return render(request, 'EditUser/student-edit.html', context)
