from django.shortcuts import redirect, render
from django.contrib import messages

from accounts.forms import AddressForm
from .models import Address, Cart, CartItems, CustomUser
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from .models import Profile

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = CustomUser.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified.')
        #     return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = CustomUser.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = CustomUser.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    
    
def cart(request):
    cart_items = CartItems.objects.filter(cart__user=request.user, cart__is_paid=False)
    context = {'cart_items': cart_items}
    return render(request,'accounts/cart.html' , context)

def checkout(request):
    cart_items = CartItems.objects.filter(cart__user=request.user, cart__is_paid=False)
    user_addresses = Address.objects.filter(user=request.user)
    
    context = {'user_addresses': user_addresses,'cart_items': cart_items}
    return render(request,'accounts/checkout.html' , context)

def remove_from_cart(request, cart_item_uid):
    cart_items = CartItems.objects.get(uid = cart_item_uid)
    cart_items.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_address(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_number = request.POST.get('contact_number')
        address_type = request.POST.get('address_type')
        street_address = request.POST.get('street_address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        landmark = request.POST.get('landmark')
        user = request.user
        # Create and save the Address instance
        address = Address(
            contact_name=contact_name,
            contact_number=contact_number,
            address_type=address_type,
            street_address=street_address,
            pincode=pincode,
            city=city,
            state=state,
            landmark=landmark,
            user=user
        )
        address.save()

        return JsonResponse({'success': True})

    return HttpResponseRedirect(request.path_info)
