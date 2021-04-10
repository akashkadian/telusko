from django.db import models

# Create your models here.
class Destination(models.Model):

    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
