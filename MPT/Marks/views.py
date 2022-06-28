from django.shortcuts import render

# Create your views here.
# make a student app, we will put marks ka url there only
def studentMarks(request):
    context = {'title': 'studentmarks'}
    return render(request, 'Marks/student-marks.html', context)