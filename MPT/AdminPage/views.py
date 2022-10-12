from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
# from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, GuardianDetails,Mentor_assign
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from EditUser.views import studentcontext
from Announcement.models import *
from accounts.models import *
from FacultyDashboard.models import *
from django.core.mail import send_mail
from MPT import settings   
from django.http import Http404
from django.template.loader import render_to_string
import datetime
import phonenumbers

# student dashboard view

# Create your views here for admin page
@staff_member_required(login_url='Login')
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def Adminpage(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {'users': users} 
        return render(request,'AdminPage/admin-user.html',context)
    else:
        return Http404("You are not authorized to view this page")

# view all the students in the database in the admin page
@user_passes_test(lambda u: u.is_superuser)
@staff_member_required(login_url='Login')
@login_required(login_url='Login')
def Adminstudent(request):
    if request.user.is_superuser:
        students = User.objects.filter(is_staff=False)
        context = {'users': students} 
        return render(request,'AdminPage/admin-student.html',context)
    else:
        return Http404("You are not authorized to view this page")

@user_passes_test(lambda u: u.is_superuser)
@staff_member_required(login_url='Login')
@login_required(login_url='Login')
def Adminmentor(request):
    if request.user.is_superuser:
        mentors = User.objects.filter(is_staff=True,is_superuser=False)
        context = {'users': mentors} 
        return render(request,'AdminPage/admin-mentor.html',context)
    else:
        return Http404("You are not authorized to view this page")

@login_required(login_url='Login')
def Activity(request):
    if request.user.is_superuser:
        return render(request,'AdminPage/admin-activities.html')
    else:
        return HttpResponse("You are not authorized to view this page")

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def deleteuser(request,id):
    if request.user.is_superuser:
        if request.method=='POST':
            # User.objects.filter(pk=id).delete()
            user=User.objects.get(pk=id)
            check=user.is_staff
            if check:
                for mentee in Mentor_assign.objects.filter(Mentor__user__usr_id=user.usr_id):
                    mentee.Mentee.user.studentprofile.is_assigned=False
                    mentee.Mentee.user.studentprofile.save()
                    user.delete()

                return redirect('admin-mentor')
            else:
                user.delete()
                return redirect('admin-student')

    return Http404("You are not authorized to view this page")

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
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
                        elif staff_status=='Inactive':
                            user.is_staff = False
                except:
                    pass
                if phonenumbers.is_valid_number(phonenumbers.parse(phone, "IN")):
                    user.phone = phone
                user.first_name = fName
                user.usr_id= stuid
                user.middle_name=Mname
                user.last_name = Lname
                user.save()

                profile.Address= Addr
                profile.religion = religion
                profile.mother_tongue = motherTongue
                profile.save()
                try:
                    details.save()
                except:
                    pass

                if user.is_staff==True:
                    try:
                        StudentProfile.objects.get(user__usr_id=usr_id).delete()
                    except:
                        pass
                else:
                    try:
                        MentorProfile.objects.get(user__usr_id=usr_id).delete()
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
                        elif staff_status=='Inactive':
                            user.is_staff = False
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
                if user.is_staff==True:
                    try:
                        StudentProfile.objects.get(user__usr_id=usr_id).delete()
                    except:
                        pass
                else:
                    try:
                        MentorProfile.objects.get(user__usr_id=usr_id).delete()
                    except:
                        pass

                return redirect('admin-mentor')
            return render(request, 'AdminPage/admin-mentor-edit.html', context)

        else:
            return HttpResponse(" You are Admin ")
    else:
        return Http404("You are not authorized to view this page")

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def Assigned(request,usr_id):
    if request.user.is_superuser:
        mentee_list = []
        for mentee in Mentor_assign.objects.filter(Mentor__user__usr_id=usr_id):
            mentee_list.append(mentee.Mentee)
        mentor = MentorProfile.objects.get(user__usr_id=usr_id)
        context={'mentor':mentor,'mentee_list':mentee_list}
        if request.POST.get('mentees'):
            mentees_id=request.POST.get('mentees')
            for mentee_id in mentees_id.split(','):
                mentee = StudentProfile.objects.get(user__usr_id=mentee_id)
                mentee.is_assigned=False
                mentee.save()
                unassign_mentee = Mentor_assign.objects.filter(Mentee__user__usr_id=mentee_id)
                try:
                    unassign_mentee.delete()  
                    # print(mentee.user.first_name,'is unassigned successfully from',mentor.user.first_name)
                except:
                    pass
        return render(request,'AdminPage/admin-assign-assigned.html',context)
    else:
        return Http404("You are not authorized to view this page")

# For assigning unassigned students :
@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
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
        return Http404("You are not authorized to view this page")

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminUpcomingMeeting(request):
    context={
         'todays_date':datetime.date.today(),
         'current_time':datetime.datetime.now().time()
    }
    return render(request, 'AdminPage/admin-meeting-upcoming.html',context)

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminPreviousMeeting(request):
    context={
         'todays_date':datetime.date.today(),
         'current_time':datetime.datetime.now().time(),
    }
    return render(request, 'AdminPage/admin-meeting-previous.html',context)

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def deleteMeetingRecord(request,id):
    if request.method=='POST':
        meeting= Meeting.objects.filter(Meeting_id=id)
        meeting.delete()
    return redirect('admin-upcoming-meeting')

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminAnnouncementTable(request):
    return render(request, 'AdminPage/admin-announcement-table.html')   

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminAnnouncementBlog(request):
    return render(request, 'AdminPage/admin-announcement-blog.html')

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminAnnouncementNew(request):
    if request.method == 'POST':
        announcement = Announcement()
        sender = request.user
        title = request.POST['title']
        content = request.POST['content']
        announcement.sender = sender
        announcement.title = title
        announcement.content = content
        announcement.save()
        send_to=request.POST['inlineRadioOptions']
        try: 
            # AnnouncementReceiver.objects.create(announcement=announcement, receiver=request.user).save()
            if send_to == 'All':
                for user_all in User.objects.all():
                    AnnouncementReceiver.objects.create(announcement=announcement, receiver=user_all).save()
                    mail_subject= str(title)
                    message= render_to_string('Announcement/announcement_email.html', {
                        'sender': 'Admin',
                        'receiver': str(user_all.first_name) + ' ' + str(user_all.last_name),
                        'announcement':content,
                        'title': title,
                    })
                    to_email= user_all.email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                    except:
                        # print('Error Occured In Sending Mail, Try Again ')
                        pass
            elif send_to == 'Facutly':
                for user_fac in MentorProfile.objects.all():
                    AnnouncementReceiver.objects.create(receiver=user_fac.user, announcement=announcement).save()
                    mail_subject= str(title)
                    message= render_to_string('Announcement/announcement_email.html', {
                        'sender': 'Admin',
                        'receiver': str(user_fac.user.first_name) + ' ' + str(user_fac.user.last_name),
                        'announcement':content,
                        'title': title,
                    })
                    to_email= user_fac.user.email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                    except:
                        # print('Error Occured In Sending Mail, Try Again ')
                        pass
            elif send_to == 'Students':
                for user_stu in StudentProfile.objects.all():
                    AnnouncementReceiver.objects.create(receiver=user_stu.user, announcement=announcement).save()
                    mail_subject= str(title)
                    message= render_to_string('Announcement/announcement_email.html', {
                        'sender': 'Admin',
                        'receiver': str(user_stu.user.first_name) + ' ' + str(user_stu.user.last_name),
                        'announcement':content,
                        'title': title,
                    })
                    to_email= user_stu.user.email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                    except:
                        # print('Error Occured In Sending Mail, Try Again ')
                        pass

        except:
            pass
        return redirect('admin-announcement-table')

    return render(request, 'AdminPage/admin-announcement-new.html')

@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url='Login')
def AdminAnnouncementDelete(request, id):
    if request.method == 'POST':
        announcement = Announcement.objects.get(id=id)
        announcement.delete()
    return redirect('admin-announcement-table')
