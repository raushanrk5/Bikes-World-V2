from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

# Create your views here.

class signup(View):
    def get(self,request):
        return render(request, './signup.html')

    def post(self,request):
        firstName = request.POST.get('Fname')
        lastName = request.POST.get('Lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')

        customer = Customer(
            fname=firstName,
            lname=lastName,
            email=email,
            password=password
        )
        error_msg = None
        values = {
            'fname': firstName,
            'lname': lastName,
            'email': email,
            'password': password,
        }

        error_msg = self.validateCustomer(customer, rePassword)
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')

        else:
            return render(request, './signup.html', {'error': error_msg, 'values': values})

    def validateCustomer(self, customer, rePassword):
        error_msg = None

        if not customer.fname:
            error_msg = 'First name required!!'

        elif len(customer.fname) < 3:
            error_msg = 'First name must be 3 char long or more!!'

        elif not customer.lname:
            error_msg = 'Last name required!!'

        elif len(customer.lname) < 3:
            error_msg = 'Last name must be 3 char long or more!!'

        elif len(customer.email) < 8:
            error_msg = 'Email must be 8 char long or more!!'

        elif not customer.password:
            error_msg = 'Password required!!'

        elif len(customer.password) < 8:
            error_msg = 'Password name must be 8 char long or more!!'

        elif customer.password != rePassword:
            error_msg = 'Both password field must match!!'

        elif customer.isExists():
            error_msg = 'Email Address already registered!!'

        return error_msg



