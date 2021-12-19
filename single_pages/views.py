from django.shortcuts import render
from mall.models import Item, Comment

def landing(request):
    recent_items = Item.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_items': recent_items
        })

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def my_page(request):
    comments = Comment.objects.filter(author=request.user)
    return render(
        request,
        'single_pages/my_page.html',
        context={'comments': comments}
    )