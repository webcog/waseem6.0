from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('category/<int:category_id>/', views.video_category, name='video_category'),
    # path('video/<int:video_id>/', views.video_detail, name='video_detail'),
]
