from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import StudentProfile
from accounts.models import User
from .models import AcademicScores
# Create your views here.

def studentMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    print(user.usr_id)
 
    context = {'title': 'studentmarks'}
    return render(request, 'Marks/student-marks.html', context)

def studentAddMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    print(user.usr_id)
 
    context = {'title': 'studentmarks'}
    return render(request, 'Marks/student-add-marks.html', context)

def studentEditMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    print(user.usr_id)
 
    context = {'title': 'studentmarks'}
    return render(request, 'Marks/student-edit-marks.html', context)

def facultyStudentMarks(request,stu_pk):

    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    
    mark = AcademicScores.objects.filter(student = student).order_by('sub_code').values()
    
    context = {'title': 'studentmarks', 'mark' : mark, 'student' : student}

    return render(request, 'Marks/faculty-student-marks.html', context)

def facultyEditMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)

    context = {'title': 'studentmarks', 'mark':mark}

    
    if request.method == 'POST':
        print("hello")
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.update(id = id, student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)
        
        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-edit-marks.html', context)

def facultyAddMarks(request,stu_pk):

    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        print("hello")
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-add-marks.html')
    