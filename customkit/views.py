from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import ChildCategory
# from carts.models import CartItem
from orders.models import OrderProduct
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from customkit.models import CustomProduct, ProductGallery_Custom
from carts.models import Cart, CartItem
from customkit.models import CartItem_Custom, Cart_Custom,CustomOrder
from orders.models import Order
from django.core.exceptions import ObjectDoesNotExist
from customkit.models import CustomLogos
from customkit.forms import CustomOrderForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from store.models import ClothingSizePants, ClothingSizeShirts
from ads.models import CreateYourOwnPagesBanners

# Create your views here.


def customkit(request):
    custom_products = CustomProduct.objects.all()
    createbanner= CreateYourOwnPagesBanners.objects.all().order_by('-id')


    context = {
        "custom_products":custom_products,
        'createbanner':createbanner,
    }
    return render(request, "customkit/customkit.html", context)


def custom_product_detail(request, product_slug):
    try:
        single_product = CustomProduct.objects.get(slug=product_slug)
        in_cart = False  # Assuming no cart functionality for custom products
    except CustomProduct.DoesNotExist:
        return HttpResponse("Product not found", status=404)

    # Product gallery
    product_gallery = ProductGallery_Custom.objects.filter(product=single_product)
    custom_logo = CustomLogos.objects.all().order_by('-id')
    pant_size = ClothingSizePants.objects.all()
    shirt_size = ClothingSizeShirts.objects.all()
    context = {
        "single_product": single_product,
        "in_cart": in_cart,
        "product_gallery": product_gallery,
        "custom_logo":custom_logo,
        'pant_size':pant_size,
        'shirt_size':shirt_size,
    }
    return render(request, "customkit/custom_product_detail.html", context)



from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomProduct
# from .models import Cart_Custom, CartItem_Custom
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def _cart_id(request):  
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required
def add_cart(request, product_id):  
    current_user = request.user  
    custom_product = CustomProduct.objects.get(id=product_id)  

    if current_user.is_authenticated:
        is_cart_item_exists = CartItem_Custom.objects.filter(custom_product=custom_product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem_Custom.objects.get(custom_product=custom_product, user=current_user)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = CartItem_Custom.objects.create(custom_product=custom_product, quantity=1, user=current_user)
    else:
        try:
            cart = Cart_Custom.objects.get(cart_id=_cart_id(request))
        except Cart_Custom.DoesNotExist:
            cart = Cart_Custom.objects.create(cart_id=_cart_id(request))
        cart.save()
        
        is_cart_item_exists = CartItem_Custom.objects.filter(custom_product=custom_product, cart=cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem_Custom.objects.get(custom_product=custom_product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = CartItem_Custom.objects.create(custom_product=custom_product, quantity=1, cart=cart)

    return redirect('custom_cart')

def remove_cart(request, product_id, cart_item_id):  
    custom_product = get_object_or_404(CustomProduct, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem_Custom.objects.get(custom_product=custom_product, user=request.user, id=cart_item_id)
        else:
            cart = Cart_Custom.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem_Custom.objects.get(custom_product=custom_product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('custom_cart')

def remove_cart_item(request, product_id, cart_item_id):  
    custom_product = get_object_or_404(CustomProduct, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem_Custom.objects.get(custom_product=custom_product, user=request.user, id=cart_item_id)
    else:
        cart = Cart_Custom.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem_Custom.objects.get(custom_product=custom_product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('custom_cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem_Custom.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart_Custom.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem_Custom.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.custom_product.price * cart_item.quantity
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'customkit/cart.html', context)

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem_Custom.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart_Custom.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem_Custom.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += cart_item.custom_product.price * cart_item.quantity
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'customkit/checkout.html', context)


# def order_product(request, product_slug):
#     product = get_object_or_404(CustomProduct, slug=product_slug)
#     if request.method == 'POST':
#         form = CustomOrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.product = product
#             order.user = request.user # Assuming the user is logged in
#             order.save()
#             return redirect('order_confirmation', order_id=order.id) # Redirect to a confirmation page
#         else:
#             # If the form is not valid, calculate the total price based on the submitted quantity
#             quantity = form.cleaned_data.get('quantity', 1) # Default to 1 if quantity is not submitted
#             total_price = product.price * quantity
#     else:
#         form = CustomOrderForm()
#         total_price = product.price # Default total price when the form is first displayed

#     return render(request, 'customkit/order_form.html', {'form': form, 'product': product, 'total_price': total_price})

























# @login_required(login_url='login')
# def order_product(request, product_slug):
#     product = get_object_or_404(CustomProduct, slug=product_slug)
#     if request.method == 'POST':
#         form = CustomOrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             quantity = form.cleaned_data.get('quantity')
#             if quantity <= 0:
#                 # If quantity is 0 or less, add an error to the form
#                 form.add_error('quantity', 'Quantity must be 1 or greater.')
#             else:
#                 order = form.save(commit=False)
#                 order.product = product
#                 order.user = request.user # Assuming the user is logged in
#                 order.save()
#                 return redirect('order_confirmation', order_number=order.order_number)

#     else:
#         form = CustomOrderForm()

#     return render(request, 'customkit/order_form.html', {'form': form, 'product': product})



















@login_required(login_url='login')
def order_product(request, product_slug):
    product = get_object_or_404(CustomProduct, slug=product_slug)
    if request.method == 'POST':
        form = CustomOrderForm(request.POST, request.FILES)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            if quantity <= 0:
                form.add_error('quantity', 'Quantity must be 1 or greater.')
            else:
                order = form.save(commit=False)
                order.product = product
                order.user = request.user
                order.save()

                user_subject = 'Order Confirmation'
                user_message = render_to_string('emails/order_confirmation.html', {'order': order})
                user_email = request.user.email
                send_mail(user_subject, strip_tags(user_message), None, [user_email], html_message=user_message)

                admin_subject = 'New Order Placed'
                admin_message = render_to_string('emails/new_order_notification.html', {'order': order})
                admin_email = 'waseemint.pk@gmail.com'
                send_mail(admin_subject, strip_tags(admin_message), None, [admin_email], html_message=admin_message)

                return redirect('order_confirmation', order_number=order.order_number)

    else:
        form = CustomOrderForm()

    return render(request, 'customkit/order_form.html', {'form': form, 'product': product})












@login_required(login_url='login')
def order_confirmation(request, order_number):
    order = get_object_or_404(CustomOrder, order_number=order_number)
    subtotal = order.order_total - order.tax
    context = {
        'order': order,
        'order_id': order.id,
        'total_price': order.order_total,
        'quantity': order.quantity,
        'address': order.full_address(),
        'name': order.full_name(),
        'order_number':order.order_number,
        'product_name': order.product.product_name,
        'product_price':order.product.price,
        'subtotal':subtotal,
        # Add any other details you want to display
    }
    return render(request, 'customkit/order_confirmation.html', context)


# from decimal import Decimal


# def calculate_total_price(request):
#     product_id = request.GET.get('product_id')
#     quantity = request.GET.get('quantity')
#     product = CustomProduct.objects.get(id=product_id)
#     total_price = product.price * int(quantity)
#     tax_rate = Decimal('0.02') # Convert the tax rate to Decimal
#     tax = total_price * tax_rate
#     total_amount_with_tax = total_price + tax
#     return JsonResponse({
#         'total_price': total_price,
#         'tax': tax,
#         'total_amount_with_tax': total_amount_with_tax
#     })

from decimal import Decimal

def calculate_total_price(request):
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')
    product = CustomProduct.objects.get(id=product_id)
    total_price = product.price * int(quantity)
    tax_rate = Decimal('0.02') # Tax rate as a Decimal
    tax = total_price * tax_rate
    total_amount_with_tax = total_price + tax
    return JsonResponse({
        'total_price': total_price,
        'tax': tax,
        'total_amount_with_tax': total_amount_with_tax
    })
