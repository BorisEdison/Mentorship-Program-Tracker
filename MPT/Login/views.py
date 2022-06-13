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
        # loggedInUser = User.objects.get(email = email)
        # print(loggedInUser.id)
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            # print('hello', loggedInUser.id)
            if request.user.is_staff:
                
                loggedInUser = MentorProfile.objects.get(user__email = email)
                print(loggedInUser.id)
                return redirect("faculty", pk = loggedInUser.id)  
                # return redirect(MentorProfile.get_absolute_url)  
               
            else:
                return redirect('/studentdashboard')
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')