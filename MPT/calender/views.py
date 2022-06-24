from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def Open_Cal(request):
    return render(request, 'calender/faculty-calendar.html')
