from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import StudentProfile, User , MentorProfile


def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        print(request.user.is_staff)
        if user:

            if request.user.is_staff == True:
                print("hello")
                auth.login(request, user)
                print("hello1")
                loggedInUser = MentorProfile.objects.get(user__email = email)
                print(loggedInUser.id)
                return redirect("faculty", pk = loggedInUser.id)  
                  
               
            else:
                print("hello2")
                auth.login(request, user)
                print("hello3")
                loggedInUser = StudentProfile.objects.get(user__email = email)
                print(loggedInUser.id)
                return redirect('student', pk = loggedInUser.id)
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')