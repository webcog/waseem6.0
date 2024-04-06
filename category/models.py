# # # from django.db import models
# # # from django.urls import reverse


# # # class Category(models.Model):
# # #     category_name = models.CharField(max_length=50, unique=True)
# # #     slug = models.SlugField(max_length=100, unique=True)
# # #     description = models.TextField(max_length=255, blank=True)
# # #     cat_image = models.ImageField(upload_to='photos/categories', blank=True)  # category image

# # #     class Meta:
# # #         verbose_name = 'category'
# # #         verbose_name_plural = 'categories'

# # #     def get_url(self):
# # #         return reverse('products_by_category', args=[self.slug])

# # #     def __str__(self):
# # #         return self.category_name

# # from django.db import models
# # from django.urls import reverse

# # class Category(models.Model):
# #     category_name = models.CharField(max_length=50, unique=True)
# #     slug = models.SlugField(max_length=100, unique=True)
# #     description = models.TextField(max_length=255, blank=True)
# #     cat_image = models.ImageField(upload_to='photos/categories', blank=True)  # category image
# #     parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories')

# #     class Meta:
# #         verbose_name = 'category'
# #         verbose_name_plural = 'categories'

# #     def get_url(self):
# #         return reverse('products_by_category', args=[self.slug])

# #     def __str__(self):
# #         return self.category_name

# # models.py

# from django.db import models
# from django.utils.text import slugify
# from django.urls import reverse

# class ParentCategory(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True,blank=True, null=True)
#     icon = models.CharField(max_length=255, default="icon fa fa-hashtag fa-fw")

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(ParentCategory, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

# class ChildCategory(models.Model):
#     name = models.CharField(max_length=100)
#     parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True,blank=True, null=True)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(ChildCategory, self).save(*args, **kwargs)
#     def get_url(self):
#         return reverse('products_by_category', args=[self.slug])
#     def __str__(self):
#         return self.name


from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    icon = models.CharField(max_length=255, default="icon fa fa-hashtag fa-fw")

    class Meta:
        verbose_name = '1 - Main Category'
        verbose_name_plural = '1 - Main Category'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MainCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class ParentCategory(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    icon = models.CharField(max_length=255, default="icon fa fa-hashtag fa-fw")

    class Meta:
        verbose_name = '2 - Parent Category'
        verbose_name_plural = '2 - Parent Category'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ParentCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.main_category} > {self.name}"

class ChildCategory(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = '3 - Child Category'
        verbose_name_plural = '3 - Child Category'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ChildCategory, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return f"{self.parent_category.main_category} > {self.parent_category} > {self.name}"

