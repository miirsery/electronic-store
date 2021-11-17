from django.shortcuts import render
from django import views

from products.models import Product


class BaseView(views.View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_active=True)
        context = {
            'products': products
        }
        return render(request, 'index.html', context=context)
