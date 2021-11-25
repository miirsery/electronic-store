from rest_framework import status
from rest_framework.response import Response

from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin

from cart.models import CartProduct, Order
from .models import Product, Review
from .serializers import ReviewSerializer


class CategoryTemplateView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category__slug=kwargs['slug'])
        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = kwargs['object']
        # hard code
        try:
            order = Order.objects.get(cart=product.cart_products.get(
                user=self.request.customer).cart)
            context['is_bought'] = order.status == Order.STATUS_COMPLITED
        except CartProduct.DoesNotExist:
            context['is_bought'] = False
        context['reviews'] = product.review_set.all()
        return context


class AddReviewProduct(APIView, CreateModelMixin):
    permissions_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['owner'] = request.customer.id

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED)
