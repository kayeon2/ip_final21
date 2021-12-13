from django.db import models
from django.contrib.auth.models import User
import os

class Item(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    price = models.CharField(max_length=10)

    head_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    brand = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.brand}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'

# Create your models here.
