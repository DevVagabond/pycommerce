from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(default=0)
    image = models.CharField(max_length=300, null=True, blank=True)
