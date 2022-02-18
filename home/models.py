import email
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100,default='1234567890')
    profile_pic=models.ImageField(default="userprofile.png",upload_to='upload/',null=True)
    date_created=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.user)
class task(models.Model):  
    owner=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    due=models.DateTimeField(auto_now=False,auto_now_add=False,null=False,blank=True)
    def __str__(self):
        return self.title

