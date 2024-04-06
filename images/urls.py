from images.views import payment_footer, return_exchange, shipping
from django.urls import path


urlpatterns = [
    path("paymetn_footer/", payment_footer, name="payment_footer"),
    path("return_exchange/", return_exchange, name="return_exchange"),
    path("shipping/", shipping, name="shipping"),
]
