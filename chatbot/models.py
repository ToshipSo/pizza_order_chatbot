from django.db import models
from random import random, seed
import time


# Create your models here.
class Response(models.Model):
    WELCOME = 0
    TAKE_PIZZA = 1
    TAKE_SIZE = 2
    TAKE_QUANTITY = 3
    TAKE_NAME = 4
    TAKE_ADDRESS = 5
    TAKE_CONFIRMATION = 6
    GET_STATUS = 7
    FALLBACK = 10

    CHOICES = (
        (WELCOME, 'Welcome'),
        (TAKE_PIZZA, 'Take Pizza'),
        (TAKE_SIZE, 'Take Size'),
        (TAKE_QUANTITY, 'Take Quantity'),
        (TAKE_NAME, 'Take Name'),
        (TAKE_ADDRESS, 'Take Address'),
        (TAKE_CONFIRMATION, 'Take Confirmation'),
        (GET_STATUS, 'Get Pizza Status'),
        (FALLBACK, 'Fallback')
    )
    response = models.CharField(max_length=200)
    context = models.PositiveSmallIntegerField(choices=CHOICES)


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Pizza, self).save(*args, **kwargs)


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
    pizza = models.ForeignKey(Pizza, related_name='pizza', on_delete=models.DO_NOTHING)
    size = models.ForeignKey(Size, related_name='pizza_size', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20, choices=STATUS, default='Placed')

    def save(self, *args, **kwargs):
        seed(int(time.time()))
        if not self.order_id:
            self.order_id = int(random() * 10000000)
        return super(Order, self).save(*args, **kwargs)

