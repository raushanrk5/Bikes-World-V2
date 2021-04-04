from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.products import Product
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order,OrderProduct

class Checkout(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, './checkout.html', {'cart_products': products})

    def post(self,request):
        country = request.POST.get('country')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        state = request.POST.get('state')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_options = request.POST.get('payment_options')
        customer=request.session.get('customer')
        cart = request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        total_price = 0
        if cart:
            for p in products:
                total_price += p.price * cart.get(str(p.id))

        order = Order(customer=Customer.objects.get(id=customer), country= country, first_name = fname, last_name = lname, state= state, shop_name= company_name, address = address, city = city, email=email, phone= phone, zip_code= zip_code, amount=total_price)
        order.save()

        for product in products:
            detail = OrderProduct(order = order, bike=product, customer=Customer.objects.get(id=customer), quantity= cart.get(str(product.id)), price= product.price)
            detail.save()
        print(payment_options)
        request.session['cart'] = {}

        return redirect('orders')
