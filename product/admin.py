from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product


class ProductAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'material', 'color', 'painting_style')
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'


admin.site.register(Product, ProductAdmin)
