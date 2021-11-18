from django.urls import path

from .views import CategoryView


urlpatterns = [
    path('category/<str:slug>', CategoryView.as_view(), name='category'),
]
