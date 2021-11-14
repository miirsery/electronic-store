from django.db import models

from utils import upload_function


class Category(models.Model):
    title = models.CharField(max_length=248)
    description = models.TextField()
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
    description = models.TextField()
    price = models.PositiveIntegerField()
    characteristic = models.TextField()
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
