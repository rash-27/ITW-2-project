from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CycleInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cycle_img = models.ImageField(upload_to='cycles')
    cycle_details = models.TextField()
    cycle_pricing = models.TextField()

    def __str__(self):
        return self.username