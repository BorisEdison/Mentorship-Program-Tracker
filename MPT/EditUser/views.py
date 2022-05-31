from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def edit(request):
    # user=User.objects.get(request.user.id)
    context={}
    # user_id = User.request.user.id

    if request.method=="POST":
        fName = request.POST['fName']
        # Lname= request.POST['Lname']
        username= request.POST['username']
        # department= request.POST['department']
        # phone= request.POST['phone']
        # email= request.POST['email']
        # email1= request.POST['email1']
        # password1= request.POST['password1']
        # password2= request.POST['password2']
        user = User.objects.get(id=request.user.id)
        user.first_name= fName
        user.save()
        return redirect('/facultydashboard')

    else:
        return render(request,'edit.html')

