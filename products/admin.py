from django.contrib import admin

from .models import (
    Product,
    Category,
    ImageGallery,
    Review
)


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery


class Review(admin.TabularInline):
    model = Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline, Review]


admin.site.register(Category)
