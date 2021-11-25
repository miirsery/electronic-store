from django.urls import path

from .views import AddReviewProduct, CategoryTemplateView, ProductDetailView


urlpatterns = [
    path('category/<str:slug>', CategoryTemplateView.as_view(), name='category'),
    path('product/add-review/', AddReviewProduct.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]
