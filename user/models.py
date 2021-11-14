from django.db import models
from django.conf import settings


class Customer(models.Model):
    '''Покупатель'''

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    # customer_orders = models.ManyToManyField(
    #     Order,  blank=True, verbose_name='Заказы покупателя', related_name='related_customer')
    # wishlist = models.ManyToManyField(
    #     Album, blank=True, verbose_name='Список ожидаемого')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
