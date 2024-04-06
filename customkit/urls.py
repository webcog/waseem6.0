from django.urls import path
from customkit import views


urlpatterns = [
    path('', views.customkit, name='customkit'),
    path('custom-product/<slug:product_slug>/', views.custom_product_detail, name='custom_product_detail'),
    path('custom_add-to-cart/<int:product_id>/', views.add_cart, name='custom_add_to_cart'),
    path('custom_remove-from-cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='custom_remove_from_cart'),
    path('custom_remove-cart-item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='custom_remove_cart_item'),
    path('custom_cart/', views.cart, name='custom_cart'),
    path('custom_checkout/', views.checkout, name='custom_checkout'),

    path('order/<slug:product_slug>/', views.order_product, name='order_product'),
    path('order/confirmation/<slug:order_number>/', views.order_confirmation, name='order_confirmation'),
    path('calculate_total_price/', views.calculate_total_price, name='calculate_total_price'),

]
    