from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse

from products.models import Product
from cart.models import Cart, CartProduct, Order
from user.models import Customer


class CartAddProductView(APIView):
    permissions_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=request.data['id'])

        cart_product, exists = CartProduct.objects.get_or_create(
            user=request.customer,
            cart=request.cart,
            content_type=ContentType.objects.get_for_model(product),
            object_id=request.data['id']
        )

        if not exists:
            cart_product.qty += 1
            cart_product.save()

        self.request.cart.save()

        return JsonResponse({'okey': 'okey'})


class CartCreateOrderView(APIView):
    permissions_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        Order.objects.create(
            customer=request.customer,
            cart=request.cart,
            **request.data
        )
        return JsonResponse({'okey': 'okey'})


class CartPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.request.cart.cartproduct_set.all()
        context['cart'] = self.request.cart

        return context
