from django.db import models

class userdetail(models.Model):
    username=models.CharField(max_length=100,default='aj')
    password=models.CharField(max_length=100,default="cm")
# Create your models here.
