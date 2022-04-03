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
        Lname= request.POST['Lname']
        Mname= request.POST['Mname']
        #username= request.POST['username']
        #department= request.POST['department']
        phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2:
            # if User.objects.filter(username=username).exists():
            #     messages.info(request, "Username Already Taken")


            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")

            else: 
                user= User.objects.create_user(password= password1, first_name=fname, email=email)
                user.save()
                return render(request, 'login-page.html')

    else: 
        messages.info(request, "Check Password")

    return render(request, 'register1.html')

def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'student_dashboard.html')
        
        else:
            message.info(request, "Check your cerdentials")

    else: 
        return render(request, 'login-page.html')


