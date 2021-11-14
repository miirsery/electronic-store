from django.contrib import admin

from .models import (
    Product,
    Category,
    ImageGallery
)


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline]


admin.site.register(Category)
