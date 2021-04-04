from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from store.models.orders import Order
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from django.http import JsonResponse

class SPayment(View):
    def get(self,request):
        return render(request, "./stripe_payment.html")