from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import BaseModel

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

class Profile(BaseModel):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    profile_image = models.ImageField(upload_to = 'profile')