from django.views.generic import ListView, DetailView
from .models import Item

class ItemList(ListView):
    model = Item
    ordering = '-pk'

class ItemDetail(DetailView):
    model = Item

# Create your views here.
