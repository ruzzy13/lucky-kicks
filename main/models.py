import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('apparel', 'Apparel'),
        ('accessories', 'Accessories'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,default="air force")
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255,choices=CATEGORY_CHOICES, default='Shoes')
    is_featured = models.BooleanField(default=False)

    # atribut sendiri
    stock = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.views > 20
        
    def increment_views(self):
        self.views += 1
        self.save()

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):
    bio = models.TextField()
    books = models.ManyToManyField(Book)
    user = models.OneToOneField(User) 