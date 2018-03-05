# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Bar, Tapes

# Register your models here.
admin.site.register(Bar)
admin.site.register(Tapes)
