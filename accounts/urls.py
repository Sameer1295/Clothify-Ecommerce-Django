from django.urls import path
from accounts.views import add_address, cart, checkout, login_page, profile,register_page, activate_email
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('register/' , register_page , name="register"),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/',cart,name='cart'),
   path('checkout/',checkout,name='checkout'),
   path('add-address/',add_address,name='add_address'),
   path('profile/', profile, name='profile'),
]