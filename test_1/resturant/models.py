from django.db import models

# Create your models here.
class Resturant(models.Model):
    name = models.CharField(unique=True, max_length=100, primary_key=True)
    address = models.CharField(max_length=500)
    phone_num = models.CharField(max_length=10)

class Reviews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resturant = models.ForeignKey(Resturant, on_delete= models.CASCADE)
    
