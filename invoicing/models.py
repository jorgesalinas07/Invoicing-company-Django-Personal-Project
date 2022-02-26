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

class Bill_Product(models.Model):
    """ Model for the conection between bill and product """
    bill_id = models.ForeignKey('Bill', on_delete=models.CASCADE,null=True, blank=True)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)
    # def __str__(self):
    #     """Return bill_id"""
    #     return self.bill_id