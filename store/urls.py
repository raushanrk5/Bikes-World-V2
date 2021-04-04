from django.urls import path
from store.views import shop, signup, login, cart, orders,checkout,details,home,stripe_payment
from store.middlewares.auth import auth_middleware

urlpatterns = [
    path('',home.Home.as_view(), name='home'),
    path('shop/', shop.Index.as_view(), name='shop'),
    path('signup/',signup.signup.as_view(), name='register'),
    path('login/',login.Login.as_view(), name='login'),
    path('logout/',login.logout, name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('checkout/',auth_middleware(checkout.Checkout.as_view()),name='checkout'),
    path('orders', auth_middleware(orders.myOrder.as_view()), name='orders'), #using auth middleware to orders
    path('bike/<name>', details.Details.as_view(), name='details'),
    path('payment/', stripe_payment.SPayment.as_view(), name="payment")
]
