from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    #username = models.CharField(max_length=264,unique=True)
    email = models.EmailField(unique=True)
    #password = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

'''class UserProfilesInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='at/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
'''
