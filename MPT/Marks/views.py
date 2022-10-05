from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import StudentProfile
from accounts.models import User
from .models import AcademicScores

def studentMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)    
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code').values()
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student}
    return render(request, 'Marks/student-marks.html', context)

def studentAddMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    context = {'title': 'studentmarks'}
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('studentMarks', pk = user.usr_id)

    return render(request, 'Marks/student-add-marks.html', context)

def studentEditMarks(request, pk,id):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    context = {'title': 'studentmarks', 'mark':mark}

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

def studentDeleteMarks(request, pk, id):
    user = User.objects.get(usr_id=pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('studentMarks',pk = user.usr_id)

def facultyStudentMarks(request,stu_pk):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    
    marks = AcademicScores.objects.filter(student = student).order_by('sub_code').values()
    
    context = {'title': 'studentmarks', 'marks' : marks, 'student' : student}

    return render(request, 'Marks/faculty-student-marks.html', context)

def facultyEditMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)

    context = {'title': 'studentmarks', 'mark':mark}

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

def facultyAddMarks(request,stu_pk):

    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)    

    if request.method == 'POST':
        scode = request.POST['sCode']
        sem = request.POST['semester']
        year = request.POST['year']
        exam = request.POST['exam']
        marks = request.POST['marks']

        AcademicScores.objects.get_or_create(student =student, academicYear = year , sem = sem , sub_code = scode , exam = exam , marks = marks)

        return redirect('facultyStudentMarks', stu_pk = user.usr_id)

    return render(request, 'Marks/faculty-add-marks.html')
    
def facultyDeleteMarks(request, stu_pk, id):
    user = User.objects.get(usr_id=stu_pk)
    student = get_object_or_404(StudentProfile, user = user)
    mark = get_object_or_404(AcademicScores, id = id)
    if request.method == 'POST':
        mark.delete()

    return redirect('facultyStudentMarks',stu_pk = user.usr_id)

