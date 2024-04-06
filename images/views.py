from django.shortcuts import render

# Create your views here.

def payment_footer(request):
    return render(request, 'payment_footer.html')

# Create your views here.

def return_exchange(request):
    return render(request, 'return_exchange.html')

def shipping(request):
    return render(request, 'shipping.html')
