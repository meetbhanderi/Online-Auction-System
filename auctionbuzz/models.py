from django.contrib.auth.models import User
from django.db import models
from time import time
from django.utils import timezone

from django.core.validators import RegexValidator

# Create your models here.

def getImage(instance, filename):
    return "auction_system/image_{0}_{1}".format(str(time()),filename)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=getImage)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default="")
    minimum_price = models.IntegerField(null=True)
    bid_end_date = models.DateField(default=None)
    created = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(default= timezone.now)


class Seller(models.Model):
    created = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(default= timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)




class Bidder(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numerics are allowed.')

    created = models.DateTimeField(default= timezone.now)
    updated = models.DateTimeField(default= timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_amount = models.CharField(max_length=255, validators=[numeric])


        

