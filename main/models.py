import uuid
from django.db import models

class Product(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,default="air force")
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255,default="shoes")
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