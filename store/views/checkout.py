from django.shortcuts import render,redirect
from store.models.products import Product
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order,OrderProduct
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from store.models.category import Category

from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

class Checkout(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        cart = request.session.get('cart')
        cart_products = []
        if cart:
            ids = list(request.session.get('cart').keys())
            cart_products = Product.get_products_by_id(ids)

        else:
            request.session['cart'] = {}
        categorys = Category.objects.all()
        return render(request, './checkout.html', {'cart_products': cart_products, 'categorys':categorys})

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
        customer=request.session.get('customer')
        cart = request.session.get('cart')
        products = []
        if cart:
            products=Product.get_products_by_id(list(cart.keys()))
        total_price = 0
        if cart:
            for p in products:
                total_price += p.price * cart.get(str(p.id))
                print(p.price)
            print(amount)

        order = Order(customer=Customer.objects.get(id=customer), country= country, first_name = fname, last_name = lname, state= state, shop_name= company_name, address = address, city = city, email=email, phone= phone, zip_code= zip_code, amount=total_price)
        order.save()

        order_products=" "
        inv = " "
        for product in products:
            detail = OrderProduct(order = order, bike=product, customer=Customer.objects.get(id=customer), quantity= cart.get(str(product.id)), price= product.price)
            detail.save()
            order_products+= str(product.name)+'\n'
            inv += str(product.id)

        print(payment_options)

        host = request.get_host()

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': order.amount,
                          # '%.2f' % order.amount.quantize(
                          #     Decimal('.01')),
            'item_name': order_products,
            'invoice': inv,
            'currency_code': 'INR',
            'notify_url': 'http://{}{}'.format(host,
                                               reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('payment_cancelled')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)

        order.invoice_id = inv
        order.save()

        request.session['order_id'] = order.id
        return render(request, './process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    request.session['cart'] = ""
    order_id = request.session.get('order_id')
    print(order_id)
    order = Order.objects.get(id=order_id)
    order.status = Order.Accepted
    payer_id = request.GET['PayerID']
    order.payer_id= payer_id
    order.save()
    print(order)
    return render(request, './payment_done.html',{'order':order})

@csrf_exempt
def payment_canceled(request):
    order_id = request.session.get('order_id')
    print(order_id)
    order = Order.objects.get(id=order_id)

    new = Order.New
    if order.status == new:
        order.delete()
    return render(request, './payment_cancelled.html')
