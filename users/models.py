from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email =  models.EmailField( unique=True)
    phone_number = models.IntegerField(unique=True)
    is_staff = models.BooleanField(default=False)