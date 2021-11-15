from django.contrib.auth.models import AnonymousUser

from user.models import Customer


class CustomerMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)
        customer = Customer.objects.get(user=request.user)
        request.customer = customer

        return self.get_response(request)
