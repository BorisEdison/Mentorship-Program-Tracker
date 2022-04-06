from audioop import reverse
import genericpath
from sre_constants import SUCCESS
from typing import Generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def Adminpage(request):
    user = User.objects.all()
    context = {'user': user} 
    return render(request, 'admin.html', context)

# def faculty(request):
#     user = User.objects.all()
#     context = {'user': user}
#     return render(request, 'faculty-dashboard.html', context)

def student(request):
    return render(request, 'student-dashboard.html')

def faculty(request):
    return render(request, 'faculty-dashboard.html')
    

def studentdetail(request, pk):
    user = User.objects.get(id=pk)
    context = {'users': user}
    return render(request, 'student-profile.html', context)

class EditView(generic.UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'edit.html'
    success_url = reverse_lazy('LoginPage')

    def get_values(self):
        return self.request.User


def edit(request):
    return render(request,'edit.html')
