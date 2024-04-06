from django.db import models

# Create your models here.

class AdBannerThree(models.Model):
    ad_image= models.ImageField(upload_to="ads/banner/")

    class Meta:
        verbose_name = 'Banner Add Images THree 438Width 240px Height'
        verbose_name_plural = 'Banner Add Images THree 438Width 240px Height'
    def __str__(self):
        return str(self.id)
    

class HomePageBannersTwo(models.Model):
    title_1=models.CharField(max_length=20)
    title_2=models.CharField(max_length=20)
    title_3=models.CharField(max_length=50)
    image = models.ImageField(upload_to="home/ads/")

    def __str__(self):
        return self.title_1
    
    class Meta:
        verbose_name = 'HomePageBannersTwo 1375px Widht 520px Height'
        verbose_name_plural = 'HomePageBannersTwo 1375px Widht 520px Height'