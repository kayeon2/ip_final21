from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Category

class ItemList(ListView):
    model = Item
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context

class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_item_count'] = Item.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        item_list = Item.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        item_list = Item.objects.filter(category=category)

    return render(
        request,
        'mall/item_list.html',
        {
            'item_list' : Item.objects.filter(category=category),
            'categories' : Category.objects.all(),
            'no_category_item_count' : Item.objects.filter(category=None).count(),
            'category' : category
        }
    )
