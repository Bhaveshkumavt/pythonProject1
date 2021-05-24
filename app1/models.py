from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator
from django.conf import settings                #import for User=settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager  #from ecom
from django.db.models.signals import pre_save,post_save                  #from ecom
from datetime import datetime                                            #from ecom


User=settings.AUTH_USER_MODEL
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"), ("married","married"), ("widow","widow")))
    gender = models.CharField(max_length=20, default="male", choices=(("Male","Male"), ("Female","Female")))
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])

    def __str__(self):
        return "%s" % self.user

    class Meta:
        db_table='profile'

    def set_data(self,n,sta,gen,age,a='default'):
        self.name=n
        self.status=sta
        self.gender = gen
        self.age = age
        self.address=a
        self.save()
        return 'done'


class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)



