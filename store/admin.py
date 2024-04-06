from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery, ClothingSizePants, ClothingSizeShirts
import admin_thumbnails 
from .models import SizeChart, FieldData

from django.contrib import admin
from .models import SizeChart, Sizes, SizeChartImage, FieldData

class SizesInline(admin.StackedInline):
    model = Sizes
    extra = 1

class SizeChartImageInline(admin.StackedInline):
    model = SizeChartImage
    extra = 1

class FieldDataInline(admin.TabularInline):
    model = FieldData
    extra = 1

@admin.register(SizeChart)
class SizeChartAdmin(admin.ModelAdmin):
    inlines = [SizesInline, SizeChartImageInline, FieldDataInline]

@admin.register(Sizes)
class SizesAdmin(admin.ModelAdmin):
    pass

@admin.register(SizeChartImage)
class SizeChartImageAdmin(admin.ModelAdmin):
    pass

@admin.register(FieldData)
class FieldDataAdmin(admin.ModelAdmin):
    pass


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category',
                    'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category',
                    'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category',
                   'variation_value', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
admin.site.register(ClothingSizeShirts)
admin.site.register(ClothingSizePants)