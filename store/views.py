from django.shortcuts import render
from django import views

from products.models import Product, Category


class BaseView(views.View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(
            is_active=True).order_by('-timestamp')
        categories = Category.objects.order_by('title')
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, 'index.html', context=context)
