from django.contrib import admin

from .models import Profile
from .models import CustomUser

admin.site.register(Profile)
admin.site.register(CustomUser)