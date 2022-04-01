from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


# Create your views here.
def user(request):
    if request.method == 'POST':
        fname= request.POST['name']
        username= request.POST['username']
        department= request.POST['department']
        phone= request.POST['phone']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Taken")
              

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")

            else: 
                user= User.objects.create_user(username=username, password= password1, first_name=fname, email=email)
                user.save()
                print("Created")
                return HttpResponse('Hello')

    else: 
        messages.info(request, "Check Password")

    return render(request, 'register.html')



