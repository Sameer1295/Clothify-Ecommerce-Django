from django.contrib import admin

from .models import Address, Cart, CartItems, Profile
from .models import CustomUser

admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Address)