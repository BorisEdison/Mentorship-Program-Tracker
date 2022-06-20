from locale import normalize
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    '''for using email as unique identifier instead of username '''

    def create_user(self,  usr_id, email, password, is_active=True, is_staff=False, is_superuser=False,first_name=None,last_name=None,middle_name=None,phone=None):

        # create and save user with email and password

        if not email:
            raise ValueError('The EMail must be set ')

        if not password:
            raise ValueError('Password is mandatory')


        User = self.model(
            email=self.normalize_email(email)
        )
        User.usr_id = usr_id
        User.is_active = is_active
        User.is_staff = is_staff
        User.is_superuser = is_superuser
        User.set_password(password)
        User.first_name=first_name
        User.last_name=last_name
        User.middle_name=middle_name
        User.phone=phone
        User.save(using=self.db)
        return User

    def create_staffuser(self, usr_id, email, password):
        User = self.create_user(
            usr_id,
            email, 
            password=password, 
            is_staff=True,
            is_superuser=False
            )
        return User


    def create_superuser(self, usr_id, email, password):
        User = self.create_user(
            usr_id,
            email,
            password=password,
            is_staff=True, 
            is_superuser=True
            )
        return User
