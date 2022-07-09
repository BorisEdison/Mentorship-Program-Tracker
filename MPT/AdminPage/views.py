from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, GuardianDetails,Mentor_assign
from django.contrib.auth.decorators import login_required
from EditUser.views import studentcontext

# student dashboard view

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
        students = User.objects.filter(is_staff=False)
        context = {'users': students} 
        return render(request,'AdminPage/admin-student.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Adminmentor(request):
    if request.user.is_superuser:
        mentors = User.objects.filter(is_staff=True,is_superuser=False)
        context = {'users': mentors} 
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

@login_required
def updateuserprofile(request,usr_id):
    if request.user.is_superuser:
        user=User.objects.get(usr_id=usr_id)
        context={'user':user}
        if not user.is_staff:
            profile = StudentProfile.objects.get(user__usr_id=usr_id)
            details,created=StudentDetails.objects.get_or_create(student_id=profile.id)
            guardian,created=GuardianDetails.objects.get_or_create(student_id=profile.id)
            context.update({
                'student': profile,
                'details':details,
                'guardian':guardian,})
            context.update(studentcontext)
            if request.method=='POST':
                fName = request.POST['fName']
                Lname = request.POST['lName']
                Mname = request.POST['mName']
                stuid = request.POST['sId']
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
                try:
                    if 'profileImg' in request.FILES:
                        profile_img = request.FILES['profileImg']
                        # if user already has profile image then delete it
                        if str(user.profile_img) != 'logo.png':
                            user.profile_img.delete()
                        user.profile_img = profile_img
                except:
                    pass
                try:
                    if request.POST['account_status']:
                        account_status = request.POST['account_status']
                        if account_status== 'Active':
                            user.is_active = True
                        else:
                            user.is_active = False
                except:
                    pass
                try:
                    if request.POST['staff_status']:
                        staff_status = request.POST['staff_status']
                        if staff_status== 'Active':
                            user.is_staff = True
                        else:
                            user.is_staff = False
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
                try:
                    details.save()
                except:
                    pass
                return redirect('admin-student')
            return render(request, 'AdminPage/admin-student-edit.html', context)
        
        elif user.is_staff and not user.is_superuser:
            profile = MentorProfile.objects.get(user__usr_id=usr_id)
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
                'user':user
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

                try:
                    if 'profileImg' in request.FILES:
                        profile_img = request.FILES['profileImg']
                        # if user already has profile image then delete it
                        if str(user.profile_img) != 'logo.png':
                            user.profile_img.delete()
                        user.profile_img = profile_img
                except:
                    pass
                try:
                    if request.POST['account_status']:
                        account_status = request.POST['account_status']
                        if account_status== 'Active':
                            user.is_active = True
                        else:
                            user.is_active = False
                except:
                    pass
                try:
                    if request.POST['staff_status']:
                        staff_status = request.POST['staff_status']
                        if staff_status== 'Active':
                            user.is_staff = True
                        else:
                            user.is_staff = False
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
                return redirect('admin-mentor')
            return render(request, 'AdminPage/admin-mentor-edit.html', context)

        else:
            return HttpResponse(" You are Admin ")
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Assigned(request,usr_id):
    if request.user.is_superuser:
        mentee_list = []
        for mentee in Mentor_assign.objects.filter(Mentor__user__usr_id=usr_id):
            mentee_list.append(mentee.Mentee)
        # print(mentee_list)
        mentor = MentorProfile.objects.get(user__usr_id=usr_id)
        context={'mentor':mentor,'mentee_list':mentee_list}
        if request.POST.get('mentees'):
            mentees_id=request.POST.get('mentees')
            for mentee_id in mentees_id.split(','):
                mentee = StudentProfile.objects.get(user__usr_id=mentee_id)
                mentee.is_assigned=False
                mentee.save()
                unassign_mentee = Mentor_assign.objects.filter(Mentee__user__usr_id=mentee_id)
                # print(mentor,mentee)
                try:
                    unassign_mentee.delete()  
                    print(mentee.user.first_name,'is unassigned successfully from',mentor.user.first_name)
                except:
                    pass
        return render(request,'AdminPage/admin-assign-assigned.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

# For assigning unassigned students :
@login_required
def Unassigned(request,usr_id):
    if request.user.is_superuser:
        mentee_list= StudentProfile.objects.filter(is_assigned=False)
        mentor = MentorProfile.objects.get(user__usr_id=usr_id)
        context={'mentor':mentor,'mentee_list':mentee_list}
        if request.POST.get('mentees'):
        # if request.method=='POST':
            mentees_id=request.POST.get('mentees')
            # mentees_id=request.POST['mentees']
            for mentee_id in mentees_id.split(','):
                assign_mentee=Mentor_assign()
                mentee = StudentProfile.objects.get(user__usr_id=mentee_id)
                assign_mentee.Mentor=mentor
                assign_mentee.Mentee=mentee
                mentee.is_assigned=True
                mentee.save()
                # print(mentor,mentee)
                try:
                    if assign_mentee.save():  
                        print(mentee.user.first_name,'is assigned successfully to',mentor.user.first_name)
                except:
                    pass
        return render(request,'AdminPage/admin-assign-unassigned.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")