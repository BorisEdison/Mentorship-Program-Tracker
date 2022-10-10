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
    exam = models.CharField(max_length=20,blank=True,null=True,choices=exam_choices,default=1)
    marks = models.IntegerField(default=50)

    class Meta():
        unique_together = [['student','sem','exam','sub_code']]
        verbose_name = "Marks"
    def __str__(self):
        return self.student.user.first_name

class SemCGPA(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentProfile,null=True,blank=True ,on_delete=models.CASCADE)
    sem = models.CharField(max_length=50, blank=True, null=True)
    cgpa = models.FloatField(default=0.0)

    class Meta():
        unique_together = [['student','sem']]
        verbose_name = "Semester CGPA"
    def __str__(self):
        return self.student.user.first_name + " " + self.sem + " " + str(self.cgpa)