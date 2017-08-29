from django.db import models

# Create your models here.
class register(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uphone=models.CharField(max_length=11)
    uemail=models.CharField(max_length=30)
    uaddress = models.CharField(max_length=100)
    uyoubian = models.CharField(max_length=6)
    ushou = models.CharField(max_length=20)