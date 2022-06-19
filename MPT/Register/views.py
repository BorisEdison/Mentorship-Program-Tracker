from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from accounts.models import StudentProfile, MentorProfile
from accounts.models import User


# Student Registration + teacher registeration as student from registeration page
def StudentRegister(request):
    if request.method == 'POST':
        fname= request.POST['name']
        Lname= request.POST['Lname']
        phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']
        mid_name= request.POST['Mname']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'Register/register.html')

            else: 
                user= User.objects.create_user(usr_id = 'asdfgghjkl', email=email, password= password1, first_name=fname, last_name=Lname,middle_name=mid_name,phone=phone)
                user.save()
                # u = User.objects.get(email=request.POST['email'])
                # profile =StudentProfile(user = u)
                # # print(request.profile)
                # profile.save()
                print("profile saved")
                return redirect('/')
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")
    context = {'page': 'StudentUser',
                'title': 'New Account'
                }
    return render(request, 'Register/register.html',context)

# Faculty Registration
def AdminRegister(request):
    
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
                return render(request, 'Register/register.html')

            else: 
                user= User.objects.create_superuser(email=email, password= password1)
                user.save()
                return redirect('/AdminPage')
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")

    context = {'page': 'SuperUser',
                'title': 'Add New Admin'
                }

    return render(request, 'Register/register.html', context)
