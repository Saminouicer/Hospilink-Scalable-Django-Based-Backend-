# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):


    ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('pharmacist', 'Pharmacist'),
    ('procurement', 'Procurement Officer'),
    ('director', 'Hospital Director'),
    ('delivery', 'Delivery Agent'),
    ('supplier', 'Supplier'),
    ('user', 'USER'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=65)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


    # USERNAME_FIELD = 'email'       # Login uses email
    # REQUIRED_FIELDS = [] 




# git commit -m'login and register using jwt'