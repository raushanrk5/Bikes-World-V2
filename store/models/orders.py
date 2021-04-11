from django.db import models
from .products import Product
from .customer import Customer
import datetime

class Order(models.Model):
    New = "New"
    Accepted = "Accepted"
    Preparing = "Preparing"
    OnShipping = "OnShipping"
    Completed = "Completed"
    STATUS_CHOICES = (
        (New, 'New'),
        (Accepted, 'Accepted'),
        (Preparing, 'Preparing'),
        (OnShipping, 'OnShipping'),
        (Completed, 'Completed'),
        # ('Canceled', 'Canceled'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, editable=True)
    last_name = models.CharField(max_length=40, editable=True)
    shop_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=70, editable=True, default="")
    zip_code = models.CharField(max_length=10, editable=False)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(blank=True, max_length=30)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice_id = models.CharField(max_length=200, default=True)
    payer_id = models.CharField(max_length=200, default=True)


    @staticmethod
    def get_customer_orders(customer_id):
        return Order.objects.filter(customer = customer_id).exclude(status= Order.New).order_by('-created_at')

    def __str__(self):
        return self.customer.fname + " " + self.customer.lname


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    bike = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bike.name

    @staticmethod
    def get_customer_orders(customer_id):
        return OrderProduct.objects.filter(customer=customer_id).order_by('-created_at')
