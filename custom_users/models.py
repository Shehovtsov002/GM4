from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    phone = models.CharField(max_length=100, unique=True, default='+996')
    date_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
