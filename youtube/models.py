from django.db import models

class CategoryVideo(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Video(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryVideo, on_delete=models.CASCADE)
    embed_code = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title