from contextlib import nullcontext
from tabnanny import verbose
from django.db import models
from accounts.models import StudentProfile
# Create your models here.

# class Exam(models.Model):
    # ia1 = models.PositiveIntegerField(null=True)
    # ia2 = models.PositiveIntegerField(null=True)
    # endsem =  models.PositiveIntegerField(null=True)

class AcademicScores(models.Model):
    exam_choices = (
        ("IA1", "IA1"),
        ("IA2", "IA2"),
        ("EndSem", "EndSem"),
    )
    
    student = models.ForeignKey(StudentProfile,null=True,blank=True ,on_delete=models.CASCADE)
    academicYear = models.CharField(max_length=50, blank=True, null=True)
    sem = models.CharField(max_length=50, blank=True, null=True)
    sub_code = models.CharField(max_length=50, blank=True, null=True)
    exam = models.CharField(max_length=20,blank=True,null=True,choices=exam_choices,default=1)
    marks = models.IntegerField(default=50)
    # exam = models.ForeignKey(Exam,null=True,blank=True, on_delete=models.CASCADE)

    class Meta():
        unique_together = [['student','sem','exam','sub_code']]
        verbose_name = "Marks"
    def __str__(self):
        return self.student.user.first_name