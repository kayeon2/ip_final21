from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ItemDetail.as_view()),
    path('', views.ItemList.as_view()),
]