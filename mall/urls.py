from django.urls import path
from . import views

urlpatterns = [
    path('update_item/<int:pk>/', views.ItemUpdate.as_view()),
    path('create_item', views.ItemCreate.as_view()),
    path('tag/<str:slug>', views.tag_page),
    path('category/<str:slug>', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('', views.ItemList.as_view()),
]