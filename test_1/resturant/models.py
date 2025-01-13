from django.db import models

# Create your models here.
class Resturant(models.Model):
    name = models.CharField(unique=True, max_length=100, primary_key=True)
    address = models.CharField(max_length=500)
    phone_num = models.CharField(max_length=10)
    rating =models.SmallIntegerField(null=False, default=0)

    def to_dict(self):
        return{
            "name":self.name,
            "address":self.address,
            "phone":self.phone_num,
            "rating":self.rating
        }

class Reviews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resturant = models.ForeignKey(Resturant, on_delete= models.CASCADE )

    

    
       
    
