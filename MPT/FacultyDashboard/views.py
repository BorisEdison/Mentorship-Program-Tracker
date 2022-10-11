from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from MPT import settings    
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, Mentor_assign, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout as django_logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from EditUser.views import studentcontext
from .models import *
from Marks.models import *
from Announcement.models import *
import datetime

#logout the logged in user
def logout(request):
    django_logout(request)
    return redirect('/')

# Create your views here.
@staff_member_required(login_url='Login')
def studentdetail(request, fac_id, stu_id):
    user = User.objects.get(usr_id=stu_id)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    faculty = User.objects.get(usr_id=fac_id)
    student = StudentProfile.objects.get(user=user)
    cgpa,created=SemCGPA.objects.get_or_create(student=student)
    cgpa_dict={}
    try:
        for i in ['I','II','III','IV','V','VI','VII','VIII']:
            cgpa_dict['SEMESTER '+i] = cgpa.__dict__['sem'+i]
    except:
        pass
    distinct_sem_yr = AcademicScores.objects.filter(student=student).values('academicYear','sem','exam').distinct().order_by('academicYear','sem','sub_code','exam')
    chartdict={}
    for i in distinct_sem_yr:
        distinct_subs=AcademicScores.objects.filter(academicYear=i['academicYear'],sem=i['sem']).values('sub_code').distinct()
        sub_code_dict={}
        for j in distinct_subs:
            sub_code_dict[j['sub_code']]=AcademicScores.objects.filter(academicYear=i['academicYear'],sem=i['sem'],sub_code=j['sub_code']).values('exam','marks')
        chartdict[str(i['academicYear'])+" SEMESTER " +str(i['sem'])]=sub_code_dict

    context =  { 'user': user,'faculty':faculty, 'student': student,'unread_announcement':unread_announcements,'chartdict':chartdict,'cgpa_dict':cgpa_dict} 
    context.update(studentcontext)

    if request.method == "POST":
        profile = StudentProfile.objects.get(user__usr_id=stu_id)
        details,created=StudentDetails.objects.get_or_create(student_id=profile.id)
        hobbies,created=StudentHobbies.objects.get_or_create(student_id=profile.id)
        guardian,created=GuardianDetails.objects.get_or_create(student_id=profile.id)
        extraCurr,created=StudentExtraCurricular.objects.get_or_create(student_id=profile.id)
        Medical,created=StudentMedicalReport.objects.get_or_create(student_id=profile.id)
        context.update({
            'student': profile,
            'pk': request.user.usr_id,
            'details':details,
            'hobbies':hobbies,
            'guardian':guardian,
            'extraCurr':extraCurr,
            'Medical':Medical})
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

        # user = User.objects.get(usr_id=stu_id)
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
        # user.usr_id= stuid
        user.middle_name=Mname
        user.last_name = Lname
        user.phone = phone
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
    
    # this is for getting the student details
    try:
        student = StudentProfile.objects.get(user=user)
        details=StudentDetails.objects.get(student_id=student.id)
        hobbies=StudentHobbies.objects.get(student_id=student.id)
        guardian=GuardianDetails.objects.get(student_id=student.id)
        Medical=StudentMedicalReport.objects.get(student_id=student.id)
        extraCurr=StudentExtraCurricular.objects.get(student_id=student.id)
        achievements=[i for i in extraCurr.achievements.split(',')]
        clubs=[i for i in extraCurr.clubs.split(',')]
        hobbies=[i for i in hobbies.hobby.split(',')]
        organizations=[i for i in extraCurr.organization.split(',')]
        context.update({'student' : student,'details':details,'hobbies':hobbies,'guardian':guardian,'clubs':clubs,'hobbies':hobbies,'achievements':achievements,'orgs':organizations,'Medical':Medical})
    except:
        pass
    # print(student.user.usr_id)
    return render(request, 'FacultyDashboard/faculty-student-profile.html', context)

@staff_member_required(login_url='Login')
def faculty(request,pk):
    if request.user.is_staff and not request.user.is_superuser:
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
        students = Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id)
        context = { 'students': students,
                    'fac_id': pk,
                    'ALL':'checked',
                    'unread_announcement':unread_announcements
                    }
        try:
            if request.method=='GET' and request.GET['inlineRadioOptions']:
                year=request.GET.get('inlineRadioOptions')
                if year != 'ALL':
                    students=Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id ,Mentee__studentdetails__current_year=year)
                    del context['ALL']
                    context['students']=students
                    context[year]='checked'
        except:
            pass
                    
        return render(request, 'FacultyDashboard/faculty-dashboard.html', context)

    else:
        return redirect(to='Login')   

@staff_member_required(login_url='Login')
def facultyMeeting(request):
    if request.user.is_staff and not request.user.is_superuser:
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
        students = Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id)
        context = { 'students': students,
                    'ALL':'checked',
                    'unread_announcement':unread_announcements
                    }
        try:
            if request.method=='GET' and request.GET['inlineRadioOptions']:
                year=request.GET.get('inlineRadioOptions')
                if year != 'ALL':
                    students=Mentor_assign.objects.filter(Mentor__user__usr_id = request.user.usr_id ,Mentee__studentdetails__current_year=year)
                    del context['ALL']
                    context['students']=students
                    context[year]='checked'
        except:
            pass
            
        if request.method=='POST':
            sender=request.user.mentorprofile
            title= request.POST['title']
            meeting_link_or_venue=request.POST['link_or_venue']
            mode=request.POST['mode']
            meeting_date=request.POST['date']
            meeting_desc=request.POST['content']
            meeting_time=request.POST['time']
            if request.POST.get('sendTo'):
                mentees_id=request.POST.get('sendTo')
                # print('mentees selected are ',mentees_id)
                for mentee_id in mentees_id.split(','):
                    newMeeting = Meeting()
                    receiver = StudentProfile.objects.get(user__usr_id=mentee_id)
                    newMeeting.Sender = sender
                    newMeeting.Receiver = receiver
                    newMeeting.Meeting_title = title
                    newMeeting.Meeting_link_or_venue = meeting_link_or_venue
                    newMeeting.Meeting_date = meeting_date
                    newMeeting.Meeting_mode=mode
                    newMeeting.Meeting_description = meeting_desc
                    newMeeting.Meeting_time = meeting_time
                    try:
                        newMeeting.save()
                        print(newMeeting.Meeting_id)
                        mail_subject= str(title)
                        message= render_to_string('FacultyDashboard/meeting_scheduled_email.html', {
                            'sender': str(sender.user.first_name) + ' ' + str(sender.user.last_name),
                            'receiver': str(receiver.user.first_name) + ' ' + str(receiver.user.last_name),
                            'meeting_title': title,
                            'meeting_link_or_venue': meeting_link_or_venue,
                            'meeting_date': meeting_date,
                            'meeting_time': meeting_time,
                            'meeting_desc': meeting_desc,
                        })
                        to_email= receiver.user.email
                        try:
                            send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                        except:
                            print('Error Occured In Sending Mail, Try Again ')
                            pass
                    except:
                        pass
            return redirect('/facultydashboard/'+str(request.user.usr_id),pk=request.user.usr_id)
        return render(request, 'FacultyDashboard/faculty-meeting.html',context)

    else:
        return redirect('Login')

@staff_member_required(login_url='Login')
def overallMeetingRecords(request):

    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    context={
         'todays_date':datetime.date.today(),
         'current_time':datetime.datetime.now().time(),
            'unread_announcement':unread_announcements
    }
    return render(request, 'FacultyDashboard/overall-meeting-records.html',context)

@staff_member_required(login_url='Login')
def deleteMeeting(request,id):
    if request.method=='POST':
        meeting= Meeting.objects.filter(Meeting_id=id)
        meeting.delete()
    return redirect('overall-meeting-records')


@staff_member_required(login_url='Login')
def meetingNotes(request,id):
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    meeting=Meeting.objects.get(Meeting_id=id)
    attendance_notes,created=MeetingAttendance.objects.get_or_create(Meeting_id=meeting)
    context={
        'meeting':meeting,
        'meetinfo':attendance_notes,
        'unread_announcement':unread_announcements
    }
    
    if request.method=='POST':
        notes=request.POST['note']
        attendance_notes.Notes=notes
        try:
            attendance=request.POST['attedance']
            if attendance=='Present':
                attendance_notes.Attendance=True
            elif attendance=='Absent':
                attendance_notes.Attendance=False
        except:
            pass
        
        attendance_notes.save()
        return redirect('overall-meeting-records')
    return render(request, 'FacultyDashboard/meeting-notes.html',context)

@staff_member_required(login_url='Login')
def induvidualMeetingRecords(request,fac_id,stu_id):
    if request.user.is_staff and not request.user.is_superuser:
        unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()        
        student=StudentProfile.objects.get(user__usr_id=stu_id)
        meetings=Meeting.objects.filter(Receiver=student)
        context={
            'student':student,
            'meetingrecords':meetings,
            'todays_date':datetime.date.today(),
            'current_time':datetime.datetime.now().time(),
            'unread_announcement':unread_announcements
        }
        return render(request, 'FacultyDashboard/induvidual-meeting-records.html',context)
    return render(request, 'FacultyDashboard/induvidual-meeting-records.html')

@staff_member_required(login_url='Login')
def individualMeetingNotes(request,fac_id,stu_id,meet_id):
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=request.user,is_read=False).count()
    meeting=Meeting.objects.get(Meeting_id=meet_id)
    attendance_notes,created=MeetingAttendance.objects.get_or_create(Meeting_id=meeting)
    context={
        'meeting':meeting,
        'meetinfo':attendance_notes,
        'unread_announcement':unread_announcements
    }
    
    if request.method=='POST':
        notes=request.POST['note']
        attendance_notes.Notes=notes
        try:
            attendance=request.POST['attedance']
            if attendance=='Present':
                attendance_notes.Attendance=True
            elif attendance=='Absent':
                attendance_notes.Attendance=False
        except:
            pass
        attendance_notes.save()
        return redirect('induvidual-meeting-records',fac_id=fac_id,stu_id=stu_id)
    return render(request, 'FacultyDashboard/meeting-notes.html',context)

@staff_member_required(login_url='Login')
def individualDeleteMeeting(request,fac_id,stu_id,meet_id):
    if request.method=='POST':
        meeting= Meeting.objects.filter(Meeting_id=meet_id)
        meeting.delete()
    return redirect('induvidual-meeting-records',fac_id=fac_id,stu_id=stu_id)