from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['title']

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )
    
    class Meta:
        ordering = ['id']


class StockProduct(models.Model):
    class Meta:
        unique_together = (('stock', 'product'),)

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
