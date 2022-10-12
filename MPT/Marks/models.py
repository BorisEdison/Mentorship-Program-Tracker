from contextlib import nullcontext
from tabnanny import verbose
from django.db import models
from accounts.models import StudentProfile

class AcademicScores(models.Model):
    exam_choices = (
        ("IA1", "IA1"),
        ("IA2", "IA2"),
        ("EndSem", "EndSem"),
    )
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentProfile,null=True,blank=True ,on_delete=models.CASCADE)
    academicYear = models.CharField(max_length=50, blank=True, null=True)
    sem = models.CharField(max_length=50, blank=True, null=True)
    sub_code = models.CharField(max_length=50, blank=True, null=True)
    sub_name = models.CharField(max_length=50, blank=True, null=True)
    exam = models.CharField(max_length=20,blank=True,null=True,choices=exam_choices,default=1)
    marks = models.IntegerField(default=0)
    outof = models.IntegerField(default=80)

    class Meta():
        unique_together = [['student','sem','exam','sub_code']]
        verbose_name = "Marks"
    def __str__(self):
        return self.student.user.first_name

class SemCGPA(models.Model):
    student = models.OneToOneField(StudentProfile,on_delete=models.SET_NULL, null=True)
    semI = models.FloatField(default=0)
    semII = models.FloatField(default=0)
    semIII = models.FloatField(default=0)
    semIV = models.FloatField(default=0)
    semV = models.FloatField(default=0)
    semVI = models.FloatField(default=0)
    semVII = models.FloatField(default=0)
    semVIII = models.FloatField(default=0)

    class Meta():
        verbose_name = "SemCGPA"

    def __str__(self):
        return self.student.user.first_name + " SemCGPA" 