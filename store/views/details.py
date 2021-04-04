from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.images import Image
from django.views import View


class Details(View):

    def get(self,request,name):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        ids = list(request.session.get('cart').keys())
        cart_products = Product.get_products_by_id(ids)
        bike = Product.objects.get(name=name)
        print(bike)
        images = Image.objects.filter(bike_id = bike)
        print(images)
        return render(request,"./detail.html",{"product":bike, "images":images, 'cart_products': cart_products})