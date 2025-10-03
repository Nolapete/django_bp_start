from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Optional: Customize the list display, filters, and search fields
    list_display = ("name", "price", "created_by")
    list_filter = ("created_by",)
    search_fields = ("name",)
