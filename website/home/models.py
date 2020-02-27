from django.db import models
from math import ceil

# Create your models here.


class Destinations(models.Model):
    name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    originalPrice = models.IntegerField()

    def __str__(self):
        return self.category

    def DiscountCalc(self):
        Discount = ceil(
            ((self.originalPrice-self.price)/self.originalPrice) * 100)
        return Discount


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="", unique=True)
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField()

    def __str__(self):
        return self.email


class Inquiry(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="", blank=False)
    email = models.EmailField(
        max_length=100, default="", blank=False,)
    contact = models.CharField(max_length=100, default="", blank=False)

    def __str__(self):
        return self.email


class Package(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    offer = models.BooleanField(default=False)
    orginalPrice = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.category

    def DiscountCalc(self):
        Discount = ceil(
            ((self.orginalPrice-self.price)/self.orginalPrice) * 100)
        return Discount


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.email
