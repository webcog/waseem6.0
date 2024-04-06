from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    total_price = 0  # Initialize total_price to 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            
            for cart_item in cart_items:
                cart_count += cart_item.quantity
                total_price += cart_item.quantity * cart_item.product.price  # Assuming you have a 'price' attribute in your Product model

        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count, total_price=total_price)
