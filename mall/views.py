from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item, Category, Tag

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

class ItemCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Item
    fields = ['title', 'hook_text', 'content', 'price', 'head_image', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(ItemCreate, self).form_valid(form)
        else:
            return redirect('/mall/')

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

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    item_list = tag.item_set.all()

    return render(
        request,
        'mall/item_list.html',
        {
            'item_list' : item_list,
            'tag': tag,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Item.objects.filter(category=None).count(),
        }
    )