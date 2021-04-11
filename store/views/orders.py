from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.orders import OrderProduct,Order
from store.models.products import Product
from store.models.customer import Customer
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from store.models.category import Category


class myOrder(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        cust=request.session.get('customer')
        customer = Customer.objects.get(id=cust)
        orders = Order.get_customer_orders(customer)
        categorys = Category.objects.all()
        print(customer,orders)

        cart = request.session.get('cart')
        product = request.POST.get('product')
        remove_from_cart = request.POST.get('remove_from_cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove_from_cart:
                    cart.pop(product)
        else:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, './order.html', {'orders':orders, 'cart_products': products, 'categorys':categorys})
