from decimal import Decimal
from django.shortcuts import get_object_or_404
from main.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product,size, quantity=1, override_quantity=False):
        product_id = str(product.id)
        size_name = str(size)

        cart_key = f"{product_id}_{size_name}"

        if cart_key not in self.cart:
            self.cart[cart_key] = {
                'quantity': 0,
                'price': str(product.price),
                'product_id': product_id,
                'size': size_name,
            }
        if override_quantity:
            self.cart[cart_key]['quantity'] = override_quantity
        else:
            self.cart[cart_key]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product, size):
        product_id = str(product.id)
        size_name = str(size)
        cart_key = f"{product_id}_{size_name}"

        if cart_key in self.cart:
            pass
