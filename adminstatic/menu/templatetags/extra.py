from django import template
from menu.models import *

register = template.Library()

@register.simple_tag
def get_cart_count():
    cartitem = CartItem.objects.filter(cart__is_paid=False, cart__checker=True).count()
    print(cartitem)
    return cartitem

@register.simple_tag
def get_total_price():
    try:
        cart = Cart.objects.get(checker=True, is_paid=False)
        return cart.get_cart_total()
    except Exception as e:
        print(e)
        
