from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRoles(models.TextChoices):
    CUSTOMER = 'Customer', 'Customer'
    ADMIN = 'Admin', 'Admin'
    VENDOR = 'Vendor', 'Vendor'

class CustomUser(AbstractUser):
    # Role field
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.CUSTOMER,
    )
    # Later add more fields
