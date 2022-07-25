from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, Mentor_assign, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
from django.contrib.auth.decorators import permission_required
from accounts.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from EditUser.views import studentcontext

#logout the logged in user
def logout(request):
    django_logout(request)
    return redirect('/')

# Create your views here.
@login_required(login_url='Login')
def studentdetail(request, fac_id, stu_id):
    user = User.objects.get(usr_id=stu_id)
    faculty = User.objects.get(usr_id=fac_id)
    context =  { 'user': user,'faculty':faculty }
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
        user.usr_id= stuid
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
    return render(request, 'FacultyDashboard/faculty-student-profile.html', context)

@login_required(login_url='Login')
def faculty(request,pk):
    if request.user.is_staff:
        ## current_user = request.user
        # user_id = current_user.id
        # print(user_id)
        print(request.user.usr_id) # this is the user id of the faculty
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


# this is for testing purpose 

def facultymarks(request):
    return render(request, 'FacultyDashboard/faculty-student-marks.html')

# def stumarks(request):
#     return render(request, 'student-marks.html')