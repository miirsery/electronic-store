from django.urls import path

from .views import CartAddProductView, CartPageView, CartCreateOrderView


urlpatterns = [
    path('add-product/', CartAddProductView.as_view()),
    path('create-order/', CartCreateOrderView.as_view()),
    path('', CartPageView.as_view())
]
