from django.urls import path
from . import views

urlpatterns = [
    path('create_item', views.ItemCreate.as_view()),
    path('tag/<str:slug>', views.tag_page),
    path('category/<str:slug>', views.category_page),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('', views.ItemList.as_view()),
]