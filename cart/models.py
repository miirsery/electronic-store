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

    def save(self, *args, **kwargs):
        self.final_price = sum(
            self.cartproduct_set.values_list('final_price', flat=True))
        self.total_products = sum(
            self.cartproduct_set.values_list('qty', flat=True))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Order(models.Model):
    STAUTS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLITED = 'complited'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STAUTS_NEW, 'New order'),
        (STATUS_IN_PROGRESS, 'Order in processing'),
        (STATUS_READY, 'Order is ready'),
        (STATUS_COMPLITED, 'The order is received by the buyer')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Pickup'),
        (BUYING_TYPE_DELIVERY, 'Delivery')
    )

    customer = models.ForeignKey(
        Customer, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE)
    address = models.CharField(
        max_length=1024, null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default=STAUTS_NEW)
    buying_type = models.CharField(
        max_length=100, verbose_name='Тип заказа', choices=BUYING_TYPE_CHOICES)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.customer}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
