from django.db import models
from .category import Category


TypeChoice = (
    ("SB", "Sports Bike"),
    ("RB", "Road Bike")
)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='bikes')
    type = models.CharField(max_length=2, choices=TypeChoice, default="RB")

    def __str__(self):
        return self.name

    @staticmethod
    def get_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_sports_bikes():
        return Product.objects.filter(type='SB')

    @staticmethod
    def get_road_bikes():
        return Product.objects.filter(type='RB')

    @staticmethod
    def get_gallery(product_id):
        prod = Product.objects.get(id=product_id)
        gall = prod.gallery.all()
        return gall