from django.contrib import admin

from .models import Bill, Product


admin.site.register(Bill)
admin.site.register(Product)