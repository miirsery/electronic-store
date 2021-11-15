from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    # customer_orders = models.ManyToManyField(
    #     Order,  blank=True, verbose_name='Заказы покупателя', related_name='related_customer')
    # wishlist = models.ManyToManyField(
    #     Album, blank=True, verbose_name='Список ожидаемого')
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
