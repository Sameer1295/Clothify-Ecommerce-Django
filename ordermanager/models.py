from django.db import models
from accounts.models import Cart, CustomUser

from ordermanager.constants import OrderStatus, PaymentStatus

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "orders")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(default=OrderStatus.IN_PROGRESS,
        max_length=254,
        blank=False,
        null=False)  
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False)
    
    def __str__(self):
        return f'Order #{self.pk}'