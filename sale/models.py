from django.db import models

from product.models import Product


class Sale(models.Model):
    created = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
