from django.views.generic.base import TemplateView

from .models import Product


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__slug=kwargs['slug'])
        return context