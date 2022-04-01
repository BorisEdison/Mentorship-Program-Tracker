from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def Adminpage(request):
    user = User.objects.all()
    context = {'user': user} 
    return render(request, 'admin.html', context)