from django.urls import path
from products.views import add_to_cart, get_product

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
    path('add-to-cart/<uid>/' , add_to_cart , name="add_to_cart"),
]
