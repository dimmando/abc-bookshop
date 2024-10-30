from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ Product model in Admin """
    list_display = (
        'ean',
        'title',
        'author',
        'category',
        'by_age',
        'price',
        'sale_price',
        'rating',
        'number_of_pages',
        'new_arrival',
        'is_sale',
        'image',
    )

    ordering = ('ean',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
