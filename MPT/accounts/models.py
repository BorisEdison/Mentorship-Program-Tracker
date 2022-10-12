from django.db import models
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    usr_id = models.CharField(max_length=50, unique=True)
    username = None
    email = models.EmailField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    profile_img = models.ImageField(
        default='logo.png', null=True, blank=True, upload_to='images/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usr_id', ]
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class StudentProfile(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    branch_choices = [
        ('Computer Engineering', 'Computer Engineering'),
        ('Electronics and Telecommunication Engineering',
         'Electronics and Telecommunication Engineering'),
        ('Information Technology', 'Information Technology'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
    ]

    Blood_grp_choices = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DateofBirth = models.DateField(max_length=50, null=True)
    Gender = models.CharField(max_length=50, null=True, choices=gender_choices)
    Blood_grp = models.CharField(
        max_length=50, null=True, choices=Blood_grp_choices)
    Branch = models.CharField(max_length=70, null=True, choices=branch_choices)
    Address = models.TextField(max_length=250, null=True)
    State = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    religion = models.CharField(max_length=50, null=True)
    mother_tongue = models.CharField(max_length=50, null=True)
    is_assigned=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.email + ' => ' + self.user.first_name)
        # return str(self.id)


class StudentDetails(models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    current_rollNo = models.PositiveIntegerField(null=True)
    AimOfLife = models.CharField(max_length=100, blank=True, null=True)
    reason_of_engg = models.CharField(max_length=50, blank=True, null=True)
    current_year = models.CharField(max_length=50, blank=True, null=True)
    Course = models.CharField(max_length=50, blank=True, null=True)
    YearOfAdmission = models.CharField(max_length=10 ,blank=True,null=True)
    Passout_year = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.current_rollNo) + ' ' + self.student.user.first_name + ' '+self.student.user.last_name


class StudentContactDetail (models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    conct_no = models.PositiveIntegerField(
        null=True, blank=True)  # we need to use phonefield

    # pip install django-phonenumber-field[phonenumbers]
    # conct_no = PhoneNumberField(null = True, blank = True) # Here

    def __str__(self):
        return self.student.user.first_name


class StudentHobbies (models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    hobby = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.student.user.first_name


class GuardianDetails(models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    father_name = models.CharField(max_length=80, null=True, blank=True)
    mother_name = models.CharField(max_length=80, null=True, blank=True)
    relationshipWithStudent = models.CharField(
        max_length=50, null=True, blank=True)
    motherHighestEducation = models.CharField(
        max_length=50, null=True,  blank=True)
    fatherHighestEducation = models.CharField(
        max_length=50, null=True, blank=True)
    motherOccupation = models.CharField(max_length=50, null=True, blank=True)
    fatherOccupation = models.CharField(max_length=50, null=True, blank=True)
    yearlyIncome = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + ' Guardian of ' + self.student.user.first_name


class StudentExtraCurricular(models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    activityName = models.CharField(max_length=100, null=True, blank=True)
    achievements = models.CharField(max_length=100, null=True, blank=True)
    clubs = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student.user.first_name


class StudentMedicalReport(models.Model):
    student = models.OneToOneField(
        StudentProfile, on_delete=models.SET_NULL, null=True)
    addiction = models.CharField(max_length=100, null=True, blank=True)
    phobia = models.CharField(max_length=100, null=True, blank=True)
    illness = models.CharField(max_length=100, null=True, blank=True)
    treatment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.student.user.first_name


class MentorProfile(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    branch_choices = [
        ('Computer Engineering', 'Computer Engineering'),
        ('Electronics and Telecommunication Engineering',
         'Electronics and Telecommunication Engineering'),
        ('Information Technology', 'Information Technology'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
    ]

    Blood_grp_choices = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DateofBirth = models.DateField(max_length=50, null=True)
    Gender = models.CharField(max_length=50, null=True, choices=gender_choices)
    Blood_grp = models.CharField(
        max_length=50, null=True, choices=Blood_grp_choices)
    Branch = models.CharField(max_length=70, null=True, choices=branch_choices)
    Address = models.TextField(max_length=250, null=True)
    City = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True, default='Maharashtra')
    Country = models.CharField(max_length=50, null=True, default='India')
    religion = models.CharField(max_length=50, null=True)
    mother_tongue = models.CharField(max_length=50, null=True)
    qualification = models.CharField(max_length=50, null=True)
    DateofJoining = models.DateField(max_length=50, null=True)
    # meeting_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.user.email)


class Mentor_assign(models.Model):
    Mentor = models.ForeignKey(
        MentorProfile, on_delete=models.CASCADE, null=True)
    Mentee = models.OneToOneField(
        StudentProfile, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Mentee.user.email + '   is assigned to    '+self.Mentor.user.email)


''' this took lot of research and time  to find the solution to the problem of 
    auto creating the profile for the user and also to add the user to the
    group of the user, with taken care that on changing status as staff adds 
    them to the group of staff. And maintains database consistency.'''


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        if instance.is_staff and not(instance.is_superuser):
            MentorProfile.objects.create(user=instance)

        if not instance.is_staff:
            StudentProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_staff and not(instance.is_superuser):
        try:
            mentor_profile = MentorProfile.objects.get(user=instance)
        except MentorProfile.DoesNotExist:
            MentorProfile.objects.create(user=instance)
        else:
            mentor_profile.save()
    elif not instance.is_staff:
        try:
            student_profile = StudentProfile.objects.get(user=instance)
        except StudentProfile.DoesNotExist:
            StudentProfile.objects.create(user=instance)
        else:
            student_profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not instance.is_staff:
        try:
            MentorProfile.objects.get(user__usr_id=instance.usr_id).delete()
        except:
            pass
    if instance.is_staff and not(instance.is_superuser):
        try:
            StudentProfile.objects.get(user__usr_id=instance.usr_id).delete()
        except:
            pass
