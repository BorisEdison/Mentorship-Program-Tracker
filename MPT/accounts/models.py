from re import M
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
    username = None
    email = models.EmailField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    superuser=models.BooleanField(default=False)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=12,null=True,blank=True)
    profile_img = models.ImageField(default='logo.png',null=True, blank=True,upload_to='images/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    @property
    def is_staff(self):
        return str(self.staff)
    
    @property
    def is_active(self):
        return str(self.active)

    @property
    def is_superuser(self):
        return str(self.superuser)

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
    current_rollNo = models.IntegerField(unique=True, null=True)
    AimForLife = models.CharField(max_length=100, blank=True, null=True)
    reason_of_engg = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    Course = models.CharField(max_length=50, blank=True, null=True)
    YearOfAdmission = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    DateofBirth = models.DateField(max_length=50, null=True)
    Gender = models.CharField(max_length=50, null=True, choices=gender_choices)
    Blood_grp = models.CharField(
        max_length=50, null=True, choices=Blood_grp_choices)
    Branch = models.CharField(max_length=70, null=True, choices=branch_choices)
    city = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.user.email +' => '+ self.user.first_name)

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
    city = models.CharField(max_length=50, null=True)
    State = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.user.email)

    # def get_absolute_url(self):
    #     return reverse("faculty", kwargs={'pk' : self.id})


class Mentor_assign(models.Model):
    Mentor = models.OneToOneField(MentorProfile, on_delete=models.SET_NULL, null=True)
    Mentee = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Mentee.user.email + '   is assigned to    '+self.Mentor.user.email)


def get_mentee(mentor):
    mentee_list = []
    for mentee in Mentor_assign.objects.filter(Mentor=mentor):
        mentee_list.append(mentee.Mentee)
        mentee_list.extend(get_mentee(mentee.Mentee))
    return mentee_list


def user_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
            instance.groups.add(auth.Group.objects.get(name='Mentor'))


def user_post_save_mentee(sender, instance, created, **kwargs):
    if created:
        if not instance.is_staff:
            instance.groups.add(auth.Group.objects.get(name='Mentee'))


''' this took lot of research and time  to find the solution to the problem of 
    auto creating the profile for the user and also to add the user to the
    group of the user, with taken care that on changing status as staff adds 
    them to the group of staff. And maintains database consistency.'''

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:

        if instance.staff:
            MentorProfile.objects.create(user=instance)
        
        if not instance.staff:
            StudentProfile.objects.create(user=instance)

# delete instance of particular profile when staff status is changed

#don't delete this, this triggers the post_save signal when a user is created and staff status is changed
@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    if StudentProfile.objects.filter(user=instance).exists():
            instance.studentprofile.delete()
    if MentorProfile.objects.filter(user=instance).exists():
            instance.mentorprofile.delete()
    if instance.staff:
        MentorProfile(user=instance).save()
    
    if not instance.staff:
        StudentProfile(user=instance).save()
