from django.urls import path
from . import views

# urls -> views -> html

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]