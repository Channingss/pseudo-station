# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Station(models.Model):
    md5 = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    conntime = models.IntegerField(blank=True, null=True)
    recitime = models.IntegerField(blank=True, null=True)
    lng = models.CharField(max_length=20, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'