from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CycleInfo(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    cycle_img = models.ImageField(upload_to='cycles')
    cycle_details = models.TextField()
    cycle_pricing = models.TextField()
    phone_no = models.CharField(max_length=12,default='N/A')

    def __str__(self):
        return str(self.username)
    
class Coins(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)