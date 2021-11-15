from django.urls import path

from .views import CartAddProductView


urlpatterns = [
    path('add-product/', CartAddProductView.as_view())
]
