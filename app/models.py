
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class data(models.Model):
    name = models.CharField(max_length=25, null=True)
    rain = models.CharField(max_length=25, null=True)
    moisture_content = models.CharField(max_length=25, null=True)
    land_size = models.CharField(max_length=25, null=True)
    place = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    water_level = models.CharField(max_length=25, null=True)
    #time = models.

    # weather description
    temperature = models.CharField(max_length=25, null=True)
    pressure = models.CharField(max_length=25, null=True)
    weatherdescription = models.CharField(max_length=30, null=True)
    cropgrown = models.CharField(max_length=25, null=True)



