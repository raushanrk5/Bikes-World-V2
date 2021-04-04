from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.images import Image
from django.views import View
import razorpay


def razor(request):
    if request.method=="POST":
        amount = 50000
        order_currency = 'INR'
        client = razorpay.client(auth=('rzp_test_cNJJxl6tCjlePr','1nWysLEJw74brOwslYMhjXOr'))
        payment = client.order.create({'amount':amount, 'currency':order_currency, 'payment_capture': '1'})