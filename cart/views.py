from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse

from products.models import Product
from cart.models import Cart, CartProduct
from user.models import Customer


class CartAddProductView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=request.data['id'])
        customer = Customer.objects.get(user=request.user)
        cart, _ = Cart.objects.get_or_create(
            owner=customer
        )
        CartProduct.objects.create(
            user=customer,
            cart=cart,
            content_type=ContentType.objects.get_for_model(product),
            object_id=request.data['id']
        )
        return JsonResponse({'okey': 'okey'})
