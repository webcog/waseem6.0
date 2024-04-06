from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ecom import views
from accounts import urls as accounts_urls
from store import urls as store_urls
from carts import urls as carts_urls
from orders import urls as orders_urls
from customkit import urls as custom_urls
from youtube import urls as youtube_urls
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from images import urls as images_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include(accounts_urls)),
    path('store/', include(store_urls)),
    path('cart/', include(carts_urls)),
    path('orders/', include(orders_urls)),
    path('create-your-own/', include(custom_urls)),
    path('tutorials/', include(youtube_urls)),
    path('images/', include(images_urls)),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
