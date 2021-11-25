from django.contrib.contenttypes.fields import GenericRelation

from django.db import models
from django.urls import reverse

from user.models import Customer
from cart.models import CartProduct

from utils import upload_function


class Category(models.Model):
    title = models.CharField(max_length=248)
    description = models.TextField(default='Описание появится позже')
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


class ImageGallery(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=upload_function)


class Product(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_function)
    description = models.TextField(default='Описание появится позже')
    price = models.DecimalField(
        max_digits=9, decimal_places=2)
    characteristic = models.TextField(default='Характеристики появятся позже')

    recommendation = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)

    cart_products = GenericRelation(
        CartProduct, related_query_name='cart_products')

    def __str__(self):
        return f'{self.id} | {self.title}'

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})


class Review(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False)
    text = models.TextField()  # todo: add images / gallery
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()

    def __str__(self):
        return f'{self.owner} | {self.product}'
