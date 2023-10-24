from pydoc import render_doc
from tkinter import E
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.models import Cart, CartItems
from products.models import Product, SizeVariant
from django.contrib.auth.decorators import login_required




def get_product(request , slug):
    try:
        product = Product.objects.get(slug =slug)
        context = {'product':product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            # price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            # context['updated_price'] = price
        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
        print(e)
        return HttpResponse("Product not found", status=404)
        
@login_required    
def add_to_cart(request):
    quantity = request.POST.get('quantity')
    size_variant = request.POST.get('size_variant')
    uid = request.POST.get('uid')
    product = Product.objects.get(uid = uid)
    
    user = request.user
    cart , _  = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item = CartItems.objects.create(cart=cart,product=product,size_variant_id=size_variant)
        
    return HttpResponse('Product added to cart')
