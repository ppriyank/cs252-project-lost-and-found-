from __future__ import unicode_literals

from django.db import models
from cs252 import  settings
# Create your models here.

ACCEPTED_FORMATS = ['%d-%m-%Y', '%d.%m.%Y', '%d/%m/%Y']


class Data(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    rollno = models.IntegerField(blank=True)
    date = models.DateField( ACCEPTED_FORMATS , blank=True)
    description = models.CharField(max_length=100, blank=True)
    status =  models.BooleanField(default=False, blank=True)
    descriptor_image = models.CharField(max_length=100, blank=True)

    def __str__(self) :
        return self.name + ' -' +  self.email

