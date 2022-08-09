from http.client import HTTPResponse
from django.shortcuts import render
from accounts.models import User
# Create your views here.

def studentMarks(request, pk):
    user = User.objects.get(usr_id=pk)
    print(user.usr_id) 
    context = {'title': 'studentmarks'}
    return render(request, 'Marks/student-marks.html', context)

def facultyStudentMarks(request,stu_pk):
    # return HTTPResponse("boris")
    # user = User.objects.get(usr_id=stu_pk)
    # print(user.usr_id) 
    # context = {'title': 'studentmarks'}
    return render(request, 'Marks/faculty-student-marks.html')