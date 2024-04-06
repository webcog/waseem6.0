# from .models import Category


# def menu_links(request):
#     links = Category.objects.all()
#     return dict(links=links)

# from .models import ParentCategory

# def categories(request):
#     categories = ParentCategory.objects.all()
#     return {'categories': categories}


# In context_processors.py

from .models import MainCategory, ParentCategory, ChildCategory

def categories_processor(request):
    main_categories = MainCategory.objects.all()
    parent_categories = ParentCategory.objects.all()
    child_categories = ChildCategory.objects.all()

    return {
        'main_categories': main_categories,
        'parent_categories': parent_categories,
        'child_categories': child_categories,
    }
