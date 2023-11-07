from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CycleInfo(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    cycle_img = models.ImageField(upload_to='cycles')
    cycle_details = models.TextField()
    cycle_pricing = models.TextField()
    phone_no = models.CharField(max_length=12,default='N/A')
    rating = models.FloatField(default=0)


    def __str__(self):
        return str(self.username)
    
class Coins(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)

class Booking(models.Model):
    uniq = models.CharField(max_length=10,unique=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    address_at = models.TextField()

class Giving(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    uniq = models.CharField(max_length=10)
    

class Transactions(models.Model):
    uniq = models.CharField(max_length=10)
    username1 = models.CharField(max_length=40)
    username2 = models.CharField(max_length=40)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    cost = models.IntegerField(default=0)
    rating = models.FloatField(default=0)


# class Reviews(models.Model):
#     username1 = models.CharField(max_length=40)
#     username2 = models.CharField(max_length=40)
#     desc1 = models.TextField()

class MutualInfo(models.Model):
    uniq = models.CharField(max_length=10)
    username1 = models.CharField(max_length=40)
    username2 = models.CharField(max_length=40)
    taken = models.BooleanField(default=False)
    given = models.BooleanField(default=False)

