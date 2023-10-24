from django.urls import path

from ordermanager.views import callback, order_payment

urlpatterns = [
    path("payment/", order_payment, name="payment"),
    path("callback/", callback, name="callback"),
]