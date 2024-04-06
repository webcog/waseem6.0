from django.contrib import admin
from customkit.models import CustomProduct, ProductGallery_Custom, Variation_Custom, CartItem_Custom, Cart_Custom, CustomLogos, CustomOrder
import admin_thumbnails
from django.utils.html import format_html


class CustomLogosAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.image.url))

    list_display = ['image_tag',]

admin.site.register(CustomLogos, CustomLogosAdmin)

# admin.site.register(CustomLogos)

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery_Custom
    extra = 1



class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category',
                    'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category',
                   'variation_value', 'is_active')
    


admin.site.register(CustomProduct, ProductAdmin)
admin.site.register(Variation_Custom, VariationAdmin)
admin.site.register(ProductGallery_Custom)
admin.site.register(CartItem_Custom)
admin.site.register(Cart_Custom)
admin.site.register(CustomOrder)
# admin.site.register(CustomProduct)

# Register your models here.
