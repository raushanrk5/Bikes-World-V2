from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.category import Category
from store.models.images import Image
from django.views import View


class Home(View):

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        ids = list(request.session.get('cart').keys())
        cart_products = Product.get_products_by_id(ids)
        products = None
        # request.session.get('cart').clear()
        categorys = Category.get_categorys()
        category_id = request.GET.get('category')
        if category_id:
            request.session['category']=category_id
            return redirect('shop')
        else:
            products = Product.get_products()
        print('you are', request.session.get('email'))
        latest_products = products[1:8]
        #print(latest_products)

        s_bikes = Product.get_sports_bikes()
        r_bikes = Product.get_road_bikes()
        #print(s_bikes, r_bikes)
        s_length = len(s_bikes)
        r_length = len(r_bikes)
        s_zipped = zip(s_bikes[:s_length//2],s_bikes[s_length//2:])
        r_zipped = zip(r_bikes[:r_length // 2], r_bikes[r_length // 2:])

        length=len(products)
        print(length)
        mid = length//2
        prod1 = products[:mid]
        prod2 = products[mid:]
        zipped = zip(prod1,prod2)
        #print(prod1,prod2,zipped)
        prod = Product.objects.get(id=7)
        gallery = Product.get_gallery(7)
        for g in gallery:
            print(g.img_url)

        return render(request,"./index.html", {'products': products, 'categorys': categorys, 'cart_products': cart_products, 'latest_products': latest_products, 's_zipped':s_zipped, 'r_zipped':r_zipped})

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
        return redirect('home')


