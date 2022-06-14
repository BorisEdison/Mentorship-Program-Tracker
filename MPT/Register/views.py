from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth import logout
from accounts.models import StudentProfile, MentorProfile
from accounts.models import User


def logout(request):
    # logout(request)
    auth.logout(request)
    return redirect('/')

# Student Registration
def StudentRegister(request):
    if request.method == 'POST':
        fname= request.POST['name']
        Lname= request.POST['Lname']
        phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'register.html')

            else: 
                user= User.objects.create_user(email=email, password= password1, first_name=fname, last_name=Lname,phone=phone)
                user.save()
                # u = User.objects.get(email=request.POST['email'])
                # profile =StudentProfile(user = u)
                # # print(request.profile)
                # profile.save()
                # print("profile saved")
                return redirect('/')
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")
    context = {'page': 'StudentUser',
                'title': 'New Account'
                }
    return render(request, 'register.html',context)

# Faculty Registration
def FacultyRegister(request):
    
    if request.method == 'POST':
        # fname= request.POST['name']
        # Lname= request.POST['Lname']
        # phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'register.html')

            else: 
                user= User.objects.create_staffuser(email=email, password= password1)
                user.save()
                # u = User.objects.get(email=request.POST['email'])
                # profile =MentorProfile(user = u)
                # # print(request.profile)
                # profile.save()
                print("Teacher saved")
                return HttpResponse("hello")
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")

    context = {'page': 'SuperUser',
                'title': 'Add New Teacher'
                }

    return render(request, 'register.html', context)