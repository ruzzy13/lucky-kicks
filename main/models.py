import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]
    
    name = models.CharField(max_length=255,default="air force");
    price = models.IntegerField();
    description = models.TextField();
    thumbnail = models.URLField();
    category = models.CharField(max_length=255,default="shoes");
    is_featured = models.BooleanField();

    # atribut sendiri
    brand = models.CharField(max_length=255,default="nike");
    stock = models.IntegerField();
    
    def __str__(self):
        return self.title
    
    # @property