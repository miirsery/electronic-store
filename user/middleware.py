from django.contrib.auth.models import AnonymousUser

from cart.models import Cart
from user.models import Customer


class CustomerMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            return

        cart, _ = Cart.objects.get_or_create(owner=customer, in_order=False)

        request.customer = customer
        request.cart = cart

        return self.get_response(request)
