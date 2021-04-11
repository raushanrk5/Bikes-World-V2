from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.category import Category
from django.views import View


class Cart(View):
    def get(self,request):
        cart = request.session.get('cart')
        cart_products = []
        if cart:
            ids = list(request.session.get('cart').keys())
            cart_products = Product.get_products_by_id(ids)

        else:
            request.session['cart'] = {}
        categorys = Category.objects.all()
        #print(products)
        return render(request, './cart.html', {'cart_products' : cart_products, 'categorys': categorys})

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
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
        return redirect('cart')

