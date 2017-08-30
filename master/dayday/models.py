
from django.db import models
import hashlib
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uphone=models.CharField(max_length=11,default='')
    uemail=models.CharField(max_length=30)
    uaddress = models.CharField(max_length=100,default='')
    uyoubian = models.CharField(max_length=6,default='')
    ushou = models.CharField(max_length=20,default='')

    def __unicode__(self):
        return self.user

    def save(self, *args,**kwargs):
        self.upwd = hashlib.sha1(self.upwd.encode('utf8')).hexdigest()
        super(UserInfo,self).save(*args,**kwargs)