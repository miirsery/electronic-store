from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from user.models import Customer


class CartProduct(models.Model):
    user = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        'Cart', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Product: {self.content_object.title} (for basket)'

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cart product'
        verbose_name_plural = 'Cart products'


class Cart(models.Model):
    owner = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        CartProduct, blank=True, related_name='related_cart')
    total_products = models.IntegerField(
        default=0)
    final_price = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(
        default=False)  # todo: create order for anonymous

    def __str__(self):
        return f'{self.id} | {self.owner}'

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
