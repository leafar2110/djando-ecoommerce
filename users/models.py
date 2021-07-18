from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

#######AbstracUser 
# username
# first_name
# last_name
# email 
# password 
# groups
# user_permissions
# is_staff
# is_active
# is_superuser
# last_login
# date_joined


##### AbstractBaseUser
# id 
# password 
# last_login




class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.firs_name, self.last_name)

class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return[]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()