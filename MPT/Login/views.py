from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import User

def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            if request.user.staff==True:
                print(user.staff)
                return redirect('/facultydashboard/'+str(user.id),pk=user.id)
               
            else:
                return redirect('/studentdashboard/'+str(user.id),pk=user.id)
        
        else:
            messages.info(request, "Check your cerdentials")
            return render(request, 'login-page.html')

    else: 
        return render(request, 'login-page.html')