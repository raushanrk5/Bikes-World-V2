from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.category import Category
from store.models.images import Image
from django.views import View
from django.contrib import messages


class Details(View):

    def get(self,request,name):
        cart = request.session.get('cart')
        cart_products = []
        if cart:
            ids = list(request.session.get('cart').keys())
            cart_products = Product.get_products_by_id(ids)

        else:
            request.session['cart'] = {}
        bike = Product.objects.get(name=name)
        print(bike)
        images = Image.objects.filter(bike_id = bike)
        print(images)
        categorys = Category.objects.all()
        return render(request,"./detail.html",{"product":bike, "images":images, 'cart_products': cart_products, 'categorys':categorys})

    def post(self, request,name):
        url = request.META.get('HTTP_REFERER')
        print(url)
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(cart)
        remove_from_cart = request.POST.get('remove_from_cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove_from_cart:
                    cart.pop(product)
                else:
                    if remove:
                        if quantity<=1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        #messages.warning(request, 'hii!')
        return redirect(url)