# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=80)
    addr = models.TextField(max_length=100)

    def __unicode__(self):
        return self.name+" "+self.addr


class Tapes(models.Model):
    """Tapes"""
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    bar = models.ForeignKey(Bar)

    def __unicode__(self):
        return self.bar.name+"-"+self.name
