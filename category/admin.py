from django.contrib import admin
# from .models import Category
from category.models import *

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('category_name',)}
#     list_display = ('category_name', 'slug')


# admin.site.register(Category, CategoryAdmin)
admin.site.register(ChildCategory)
admin.site.register(ParentCategory)
admin.site.register(MainCategory)