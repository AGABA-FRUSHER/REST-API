from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_quantity = models.PositiveIntegerField()

# Create your models here.
