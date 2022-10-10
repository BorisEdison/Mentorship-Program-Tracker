from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import StudentProfile
from accounts.models import User
from Announcement.models import *
from FacultyDashboard.models import *
from .models import AcademicScores
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

marks_context={
    'exam_list':[
        'IA1',
        'IA2',
        'ESE'
    ],

    'year_list':[
        'FE',
        'SE',
        'TE',
        'BE'
    ],
    'sem_list':[
        'I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'VIII'
    ],
}
@login_required(login_url='Login')
def studentMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)    
    unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code','exam').values()
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student, 'unread_announcement':unread_announcements,'unseen_meetings':unseen_meetings}
    context.update(marks_context)
    return render(request, 'Marks/student-marks.html', context)

@login_required(login_url='Login')
def studentAddMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)    
    unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()
    context = {'title': 'studentmarks', 'student' : student, 'unread_announcement':unread_announcements,'unseen_meetings':unseen_meetings}
    context.update(marks_context)

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('studentMarks', pk = user.usr_id)

    return render(request, 'Marks/student-add-marks.html', context)

@login_required(login_url='Login')
def studentAddCGPA(request,):
    return render(request, 'Marks/student-add-cgpa.html')

@login_required(login_url='Login')
def studentEditMarks(request, pk,id):
    user = User.objects.get(usr_id=pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)    
    unseen_meetings=Meeting.objects.filter(Receiver=student,is_read=False).count()

    mark = get_object_or_404(AcademicScores, id = id)
    context = {'title': 'studentmarks', 'mark':mark, 'student' : student, 'unread_announcement':unread_announcements,'unseen_meetings':unseen_meetings}
    context.update(marks_context)

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']
        try:
            Edit = AcademicScores.objects.get(id = id)
            Edit.student = student
            Edit.academicYear = year
            Edit.sem = sem
            Edit.sub_code = scode
            Edit.exam = exam
            Edit.marks = marks
            Edit.save()
        except:
            pass
        return redirect('studentMarks', pk = user.usr_id)

    return render(request, 'Marks/student-edit-marks.html', context)

@login_required(login_url='Login')
def studentDeleteMarks(request, pk, id):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('studentMarks',pk = user.usr_id)

@staff_member_required(login_url='Login')
def facultyStudentMarks(request,stu_pk):
    user = User.objects.get(usr_id=stu_pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)    
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code','-exam').values()
    
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student, 'unread_announcement':unread_announcements}
    context.update(marks_context)
    return render(request, 'Marks/faculty-student-marks.html', context)

@staff_member_required(login_url='Login')
def facultyEditMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)

    context = {'title': 'studentmarks', 'mark':mark,'unread_announcement':unread_announcements}
    context.update(marks_context)

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']
        try:
            Edit = AcademicScores.objects.get(id = id)
            Edit.student = student
            Edit.academicYear = year
            Edit.sem = sem
            Edit.sub_code = scode
            Edit.exam = exam
            Edit.marks = marks
            Edit.save()      
        except:
            pass  

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-edit-marks.html', context)

@staff_member_required(login_url='Login')
def facultyAddMarks(request,stu_pk):
    user = User.objects.get(usr_id=stu_pk)
    unread_announcements=AnnouncementReceiver.objects.filter(receiver=user,is_read=False).count()
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-add-marks.html', {'unread_announcement':unread_announcements})
    
@login_required(login_url='Login')
def facultyAddCGPA(request,):
    return render(request, 'Marks/faculty-add-cgpa.html')

@staff_member_required(login_url='Login')
def facultyDeleteMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('facultyStudentMarks',stu_pk = user.usr_id)

