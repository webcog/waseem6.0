from store.models import Product

def products(request):
    products = Product.objects.all()
    return {"products":products}