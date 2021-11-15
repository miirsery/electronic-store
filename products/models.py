from django.db import models

from utils import upload_function


class Category(models.Model):
    title = models.CharField(max_length=248)
    description = models.TextField(default='Описание появится позже')
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


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

    def __str__(self):
        return f'{self.id} | {self.title}'
