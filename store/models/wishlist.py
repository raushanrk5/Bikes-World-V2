from django.db import models
from .customer import Customer
from .products import Product

class WishList(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    wished_bike = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod

    def get_categorys():
        return Category.objects.all()