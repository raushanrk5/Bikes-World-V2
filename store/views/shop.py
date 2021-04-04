from django.shortcuts import render,redirect
from store.models.products import Product
from store.models.category import Category
from django.views import View

class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
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
        print(request.session['cart'])
        return redirect('shop')

    def get(self, request, slug=None):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        ids = list(request.session.get('cart').keys())
        cart_products = Product.get_products_by_id(ids)
        products = None
        #request.session.get('cart').clear()
        categorys = Category.get_categorys()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_products_by_category(category_id)

        else:
            products = Product.get_products()
        # print('you are', request.session.get('email'))


        return render(request, './grid.html', {'products': products, 'categorys': categorys, 'cart_products': cart_products})


