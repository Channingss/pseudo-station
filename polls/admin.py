# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Station

class StationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['content']}),
        ('location', {'fields':['lat'],'classes': ['collapse']}),
    ]

admin.site.register(Station,StationAdmin)