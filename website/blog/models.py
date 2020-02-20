
from django.db import models

# Create your models here.


class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.TextField()
    head1 = models.CharField(max_length=500, blank="True")
    chead1 = models.TextField(blank="True")
    head2 = models.CharField(max_length=500, blank="True")
    chead2 = models.TextField(blank="True")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='pics', default="")
    images = models.ImageField(upload_to='blog/pics', blank="True")
    author = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title
