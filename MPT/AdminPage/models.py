from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=10, null=True)
    course = models.CharField(max_length=20, null=True)
    YearOfAdmission = models.IntegerField( null=True)
    current_RollNo = models.IntegerField( null=True)
    AimForLife = models.CharField(max_length=250, null=True)
    Reason_of_eng = models.CharField(max_length=20, null=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.current_RollNo)
