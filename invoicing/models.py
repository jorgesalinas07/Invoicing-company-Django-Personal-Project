from django.db import models

from users.models import Client
from tkinter import CASCADE
from django.db import models


class Product(models.Model):
    """ Model for the product with N:N relation with bills """
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, blank=True)
    def __str__(self):
        """Return name"""
        return self.name


class Bill(models.Model):
    """ Model for bills with 1:N relation with bills and N:N with products"""
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,null=True, blank=True)
    company_name = models.CharField(max_length=150, blank=True)
    nit = models.PositiveIntegerField(null=False, max_length=10)
    code = models.PositiveIntegerField(null=True)
    product = models.ManyToManyField(Product)
    def __str__(self):
        """Return company name"""
        return self.company_name

# >>> bill = Bill.objects.create(company_name='HTS', nit=12564, code=31664)
# >>> bill.save()
# >>> Product.objects.all()
# <QuerySet [<Product: Tamesis>, <Product: Coca cola>, <Product: Pan>]>
# >>> Product.objects.get(pk=1)
# <Product: Tamesis>

# >>> bill.product.add(1,2)

# >>> bill.product.all()
# <QuerySet [<Product: Tamesis>, <Product: Coca cola>]>
# >>> Product.objects.all()
# <QuerySet [<Product: Tamesis>, <Product: Coca cola>, <Product: Pan>]>
# >>> q=Product.objects.all()
# >>> q.name
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'QuerySet' object has no attribute 'name'
# >>> q=Product.objects.all()
# >>> q.get(pk=1).name
# 'Tamesis'