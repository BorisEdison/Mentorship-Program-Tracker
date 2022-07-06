from django.db import models
from accounts.models import StudentProfile
# Create your models here.

class AcademicScores(models.Model):
    student = models.ManyToManyField(StudentProfile)
    academicYear = models.CharField(max_length=50, blank=True, null=True)
    sem = models.CharField(max_length=50, blank=True, null=True)
    sub_code = models.CharField(max_length=50, blank=True, null=True)
    ia1 = models.PositiveIntegerField(null=True)
    ia2 = models.PositiveIntegerField(null=True)
    endsem =  models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.student.user.first_name
    
