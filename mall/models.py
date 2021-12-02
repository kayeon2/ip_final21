from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    price = models.CharField(max_length=10, blank=True)
    head_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'

# Create your models here.
