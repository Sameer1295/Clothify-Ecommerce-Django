from pydoc import render_doc
from tkinter import E
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Cart, CartItems
from products.models import Product, SizeVariant




def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
        print(e)
        
        
def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart , _  = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item = CartItems.objects.create(cart=cart,product=product,)
    
    if variant:
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))