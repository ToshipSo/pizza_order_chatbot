from django.db import models
from random import random, seed
import time


# Create your models here.
class Response(models.Model):
    WELCOME = 0
    TAKE_ORDER = 1
    TAKE_SIZE
    TAKE_TOPPINGS = 2

    CHOICES = (
        (0, 'Welcome'),
        (1, 'Take Order'),
    )
    response = models.CharField(max_length=200)
    context = models.PositiveSmallIntegerField(choices=CHOICES)


class Toppings(models.Model):
    topping = models.CharField(max_length=15)
    price = models.IntegerField()

    def __str__(self):
        return self.topping

    def save(self, *args, **kwargs):
        self.topping = self.topping.lower()
        return super(Toppings, self).save(*args, **kwargs)


class Size(models.Model):
    size = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.size

    def save(self, *args, **kwargs):
        self.size = self.size.lower()
        return super(Size, self).save(*args, **kwargs)


class Order(models.Model):
    STATUS = (
        ('Placed', 'Placed'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    order_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()
    toppings = models.ManyToManyField(Toppings, related_name='toppings', null=True)
    size = models.ForeignKey(Size, related_name='pizza_size', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=STATUS, default='Placed')
    date_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        seed(int(time.time()))
        self.order_id = int(random() * 10000000)
        return super(Order, self).save(*args, **kwargs)
