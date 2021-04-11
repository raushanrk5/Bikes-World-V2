from django import template
from store.models.category import Category
register = template.Library()
from store.models.orders import OrderProduct

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        #print(type(id),type(product.id))
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        #print(type(id),type(product.id))
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name='cart_total_price')
def cart_total_price(products,cart):
    sum=0;
    for p in products:
        sum+=price_total(p,cart)
    return sum

@register.filter(name='currency')
def currency(number):
    return '₹'+str(number)

@register.filter(name='multiply')
def multiply(number,number1):
    return number*number1

@register.filter(name='convert')
def convert(rupee):
    price = rupee/100000
    return '₹'+str(price)+ ' L'

@register.filter(name='gallery')
def gallery(product):
    gall = product.gallery.all().reverse()
    return gall[0:2]


