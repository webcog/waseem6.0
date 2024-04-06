from django.shortcuts import render
from store.models import Product, ReviewRating
from youtube.models import Video
from ads.models import AdBannerThree, HomePageBannersTwo

def home(request):
    reviews = None
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    videos = Video.objects.all().order_by('-id')
    ad_banner_three = AdBannerThree.objects.all().order_by('-id')
    homepagebanner = HomePageBannersTwo.objects.all().order_by('-id')
    banners = HomePageBannersTwo.objects.all()[:2]  # Get first two banners

    context = {'products': products,
               'reviews': reviews,
               'videos':videos,
               'ad_banner_three':ad_banner_three,
               'homepagebanner':homepagebanner,
               'banners':banners,
               }
    return render(request, 'home.html',context)
