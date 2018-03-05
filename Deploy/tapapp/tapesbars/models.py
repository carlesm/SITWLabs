# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.

class Bar(models.Model):
    name = models.CharField(max_length=80)
    addr = models.TextField(max_length=100)

    def __unicode__(self):
        return self.name+" "+self.addr

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('Bars_Detail', args=[str(self.id)])


class Tapes(models.Model):
    """Tapes"""
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    bar = models.ForeignKey(Bar)

    def __unicode__(self):
        return self.bar.name+"-"+self.name
