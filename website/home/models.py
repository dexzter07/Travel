from django.db import models

# Create your models here.


class Destinations(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(blank=True)

    def __str__(self):
        return self.category


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.TextField()

    def __str__(self):
        return self.name
