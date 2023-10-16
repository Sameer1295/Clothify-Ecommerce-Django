from django.urls import path
from accounts.views import remove_from_cart
from products.views import add_to_cart, get_product

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
    path('add-to-cart/<uid>/' , add_to_cart , name="add_to_cart"),
    path('remove-from-cart/<cart_item_uid>/', remove_from_cart, name="remove_from_cart")
]
