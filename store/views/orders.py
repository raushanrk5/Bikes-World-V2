from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.orders import Order
from django.views import View
from store.middlewares.auth import auth_middleware
#from django.utils.decorators import method_decorator

class myOrder(View):
    #@method_decorator(auth_middleware)
    def get(self,request):
        #customer=request.session.get('customer')
        #orders = Order.get_customer_orders(customer)
        #print(customer,orders)
        return render(request, './order.html')
