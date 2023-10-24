import json
from django.shortcuts import render
from accounts.models import Cart

from ordermanager.models import Order
from .constants import PaymentStatus
import environ
import razorpay
from django.views.decorators.csrf import csrf_exempt

env = environ.Env()
# Create your views here.

def order_payment(request):
    if request.method == "POST":
        amount = 1000
        client = razorpay.Client(auth=(env('RAZORPAY_KEY_ID'), env('RAZORPAY_KEY_SECRET')))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(
            user=request.user, total=amount, cart_id='3fcf4ace35fd413ca420c64b22f653f6',razorpay_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "accounts/payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/ordermanager/callback/",
                "razorpay_key": env('RAZORPAY_KEY_ID'),
                "order": order,
            },
        )
    return render(request, "accounts/payment.html")

@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(env('RAZORPAY_KEY_ID'), env('RAZORPAY_KEY_SECRET')))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        razorpay_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(razorpay_order_id=razorpay_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.payment_status = PaymentStatus.SUCCESS
            order.save()
            
            cart = Cart.objects.filter(id=order.cart_id)
            cart.is_paid = True
            cart.save()
            
            return render(request, "accounts/callback.html", context={"status": order.status})
        else:
            order.payment_status = PaymentStatus.FAILURE
            order.save()
            return render(request, "accounts/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        razorpay_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(razorpay_order_id=razorpay_order_id)
        order.payment_id = payment_id
        order.payment_status = PaymentStatus.FAILURE
        order.save()
        return render(request, "accounts/callback.html", context={"status": order.status})