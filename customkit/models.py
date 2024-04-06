from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import Account
from django.utils.html import mark_safe
from store.models import Product
from django.utils import timezone
from decimal import Decimal
import uuid

class CustomLogos(models.Model):
    image = models.ImageField(upload_to="photos/custom_logos")

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
    
    def __str__(self):
        return self.image.url
    
    


class CustomProduct(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)  # Add slug field
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.IntegerField(default=0)
    custom_text = models.CharField(max_length=200, blank=True, null=True)  # Field for custom text
    custom_logo = models.ImageField(upload_to='photos/logos/', blank=True, null=True)  # Field for custom logo
    images = models.ImageField(upload_to='photos/custom_products')
    images_hover = models.ImageField(upload_to='photos/custom_products_hover')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_order_url(self):
        return reverse('order_product', args=[self.slug])
    
    def save(self, *args, **kwargs):
        # Generate slug before saving
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('custom_product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name


class VariationManager_Custom(models.Manager):
    def colors(self):
        return super(VariationManager_Custom, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager_Custom, self).filter(variation_category='size', is_active=True)


variation_category_choise_Custom = (
        ('color', 'color'),
        ('size', 'size'),
    )


class Variation_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choise_Custom)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    objects = VariationManager_Custom()

    def __str__(self):
        return self.variation_value



class ProductGallery_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/custom_products/', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'


class Cart_Custom(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id



class CartItem_Custom(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    custom_product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation_Custom, blank=True)
    cart = models.ForeignKey(Cart_Custom, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.custom_product)
    


class CustomOrder(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )
    SIZES = (
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL","XL"),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    sizes = models.CharField(max_length=10, choices=SIZES, default="S")
    quantity = models.IntegerField(default=1)
    stuff = models.FileField(upload_to='custom_stuff', max_length = 100)
    order_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_address(self):
        return f"{self.address_line_1} {self.address_line_2}"
    
    def calculate_total_price(self):
        # Assuming the product price is stored in the CustomProduct model
        # and is accessible via the product field in the CustomOrder model
        total_price = self.product.price * self.quantity
        return total_price
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"
        # Convert the tax rate to Decimal to ensure compatibility with the price field
        tax_rate = Decimal('0.02')
        # Calculate the tax and order total using Decimal for precision
        self.tax = self.product.price * tax_rate * self.quantity
        self.order_total = self.product.price * self.quantity + self.tax
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


    

