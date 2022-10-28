from email import message
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import HttpResponse
from accounts.models import StudentProfile, MentorProfile
from accounts.models import User
from django.contrib.auth.decorators import login_required
import phonenumbers
# from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.core.mail import send_mail
from MPT import settings    
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string



# Student Registration + teacher registeration as student from registeration page
def StudentRegister(request):
    context = {'page': 'StudentUser',
                'title': 'New Account'
                }
    if request.method == 'POST':
        fname= request.POST['name']
        Lname= request.POST['Lname']
        phone= request.POST['phone']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']
        usrID= request.POST['usrID']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                try:
                    existing_user = User.objects.get(email=email)
                    if (existing_user.is_active == False):
                        existing_user.delete()
                    else:
                        messages.error(request, "This email is already registered.")
                except:
                    pass
                return render(request, 'Register/register.html',context)

            elif User.objects.filter(usr_id=usrID).exists():
                messages.info(request, "User ID Already Exists")
                return render(request, 'Register/register.html',context)

            else: 
                if phonenumbers.is_valid_number(phonenumbers.parse(phone, "IN")):
                    user= User.objects.create_user(usr_id = usrID, email=email, password= password1, is_active=False, first_name=fname, last_name=Lname,phone=phone)
                    user.save()
                    current_site= get_current_site(request)
                    mail_subject= 'Activate your account.'
                    message= render_to_string('Register/acc_activate_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    to_email= email
                    try:
                        send_mail(subject=mail_subject,message= message, from_email= settings.EMAIL_HOST_USER,recipient_list= [to_email], fail_silently=False)
                        messages.success(request, "Account Activation link has been sent to your inbox")
                        return redirect('/')
                    except:
                        messages.info(request, 'Error Occured In Sending Mail, Try Again ')
                        return redirect('/')
                else:
                    messages.info(request, 'Invalid Phone Number')
                    return render(request, 'Register/register.html',context)
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")
    
    return render(request, 'Register/register.html',context)

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user= User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user= None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active= True
        user.save()
        messages.success(request, "Your email address is now verified!!!")
        return redirect('/')

# Faculty Registration
@login_required(login_url='Login')
def FacultyRegister(request):
    if request.method == 'POST':
        # fname= request.POST['name']
        # Lname= request.POST['Lname']
        # phone= request.POST['phone']
        usr_id= request.POST['usr_id']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'Register/register.html')

            else: 
                user= User.objects.create_staffuser(usr_id = usr_id, email=email, password= password1)
                user.save()
                return redirect('/AdminPage')
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")

    context = {'page': 'SuperUser',
                'title': 'Add New Teacher',
                'action': 'Add-Faculty'
                }

    return render(request, 'Register/register.html', context)


# Faculty Registration
@login_required(login_url='Login')
def AdminRegister(request):
    if request.method == 'POST':
        # fname= request.POST['name']
        # Lname= request.POST['Lname']
        # phone= request.POST['phone']
        usr_id= request.POST['usr_id']
        email= request.POST['email']
        email1= request.POST['email1']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2 and email==email1:
                
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return render(request, 'Register/register.html')

            else: 
                user= User.objects.create_superuser(usr_id = usr_id, email=email, password= password1)
                user.save()
                return redirect('/AdminPage')
 
        else: 
            if password1!=password2:
                messages.info(request, "Password does not match")
            else:
                messages.info(request, "Email does not match")

    context = {'page': 'SuperUser',
                'title': 'Add New Admin',
                'action': 'Add-Admin'

                }

    return render(request, 'Register/register.html', context)
