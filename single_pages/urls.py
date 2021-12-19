from django.urls import path
from . import views

urlpatterns = [
    path('my_page/', views.my_page),
    path('about_me/', views.about_me),
    path('', views.landing),
]