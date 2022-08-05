from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login as auth_login
from accounts.models import User

def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                
                if request.user.is_superuser ==True:
                    if request.GET.get('next',None):
                        try:
                            if request.GET.get('pk')==user.usr_id:
                                return redirect(request.GET['next'])
                        except:
                            pass
                    return redirect('/AdminPage')

                elif request.user.is_staff==True:
                    if request.GET.get('next',None):
                        try:
                            if request.GET.get('pk')==user.usr_id:
                                return redirect(request.GET['next'])
                        except:
                            pass
                    return redirect('/facultydashboard/'+str(user.usr_id),pk=user.usr_id)
                
                else:
                    if request.GET.get('next',None):
                        try:
                            if request.GET.get('pk')==user.usr_id:
                                return redirect(request.GET['next'])
                        except:
                            pass
                    return redirect('/studentdashboard/'+str(user.usr_id),pk=user.usr_id)
            else:
                messages.info(request, 'Activate Your Account First then try to login...')
        
        else:
            if User.objects.filter(email=email).exists() and User.objects.filter(email=email).first().is_active==False:
                messages.info(request, 'Activate Your Account First then try to login...')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Password is incorrect...')
            else:
                messages.info(request,'Email is not registered... Kindly Register It First...')
                return redirect(to='register')
            return render(request, 'Login/login-page.html')

    elif request.user.is_authenticated:
        if request.user.is_superuser ==True:
            return redirect('/AdminPage')
        elif request.user.is_staff==True:
            return redirect('/facultydashboard/'+str(request.user.usr_id),pk=request.user.usr_id)
        else:
            return redirect('/studentdashboard/'+str(request.user.usr_id),pk=request.user.usr_id)
    else: 
        return render(request, 'Login/login-page.html')

@login_required(login_url='Login')
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    updated=''
    user=request.user
    if request.method == 'POST':
        curr_pass=request.POST['curr_pass']
        new_pass=request.POST['new_pass']
        conf_pass=request.POST['confirm_pass']
        try:
            if user.check_password(curr_pass):
                    user.set_password(new_pass)
                    user.save()
                    updated='yes' # password updated successfully
            else:
                updated='curr_incorrect' # current password is incorrect
        except:
            updated='no' # something went wrong
    return render(request,'change-password.html',{'updated':updated})