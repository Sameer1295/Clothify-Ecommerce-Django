from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email
from products.models import ColorVariant, Product, SizeVariant

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
    
    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid = False, cart__user = self.user).count()

    def __str__(self) -> str:
        return self.user
@receiver(post_save , sender = CustomUser)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)


class Cart(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "carts")
    is_paid = models.BooleanField(default=False)
    
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        price = []
        for cart_item in cart_items:
            price.append(cart_item.product.price)
            if cart_item.color_variant:
                color_variant_price = cart_item.color_variant.price
                price.append(color_variant_price)
            if cart_item.size_variant:
                size_variant_price = cart_item.size_variant.price
                price.append(size_variant_price)    
        print(price)
        return 1000
    
    def __str__(self) -> str:
        return 'Cart - '+str(self.user)
class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, blank=True)
    size_variant = models.ForeignKey(SizeVariant,on_delete=models.SET_NULL,null=True,blank=True)
    color_variant = models.ForeignKey(ColorVariant,on_delete=models.SET_NULL,null=True,blank=True)
    
    def get_product_price(self):
        price = [self.product.price]
        
        if self.color_variant:
            color_variant_price = self.color_variant.price
            price.append(color_variant_price)
        if self.size_variant:
            size_variant_price = self.size_variant.price
            price.append(size_variant_price)
        return sum(price)
    
    def primary_image(self):
        return self.product_images.first() 
    
    def __str__(self) -> str:
        return self.product.product_name
    
from django.db import models
from django.contrib.auth.models import User

# Create a model for user addresses
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    ADDRESS_TYPE_CHOICES = [
        ('home', 'Home'),
        ('work', 'Work'),
    ]
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    street_address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.contact_name} - {self.street_address}, {self.city}, {self.state}"
