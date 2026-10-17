from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Define the roles
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('operator', 'Operator'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
