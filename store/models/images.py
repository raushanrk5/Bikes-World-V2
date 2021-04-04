from django.db import models
from .products import Product


class Image(models.Model):
    bike_id = models.ManyToManyField(Product,related_name='gallery')
    image = models.ImageField(blank=True, null=True, upload_to='uploads/images')
    img_url = models.URLField(blank=True, null=True, max_length=2000)

