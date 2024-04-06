# from django.shortcuts import render
# from .models import Video

# def video_list(request):
#     videos = Video.objects.all()
#     context = {'videos': videos}
#     return render(request, 'youtube/video_list.html', context)

# def video_category(request, category):
#     videos = Video.objects.filter(category=category)
#     context = {'videos': videos, 'category': category}
#     return render(request, 'youtube/video_category.html', context)

# def video_detail(request, video_id):
#     video = Video.objects.get(pk=video_id)
#     return render(request, 'youtube/video_detail.html', {'video': video})

from django.shortcuts import render
from .models import Video, CategoryVideo

def video_list(request):
    videos = Video.objects.all()
    categories = CategoryVideo.objects.all()
    context = {'videos': videos, 'categories': categories}
    return render(request, 'youtube/video_list.html', context)


def video_category(request, category_id):
    categories = CategoryVideo.objects.all()
    category = CategoryVideo.objects.get(pk=category_id)
    videos = Video.objects.filter(category=category)
    context = {'videos': videos, 'category': category, 'categories':categories}
    return render(request, 'youtube/video_category.html', context)

# def video_detail(request, video_id):
#     video = Video.objects.get(pk=video_id)
#     return render(request, 'youtube/video_detail.html', {'video': video})
