from django.db import models
from django.urls import reverse

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cbv_app:shop_detail',kwargs={'pk':self.pk})

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    shop = models.ForeignKey(Shop,related_name="shops",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
