# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .models import Bar, Tapes

# Create your views here.

class BarListView(generic.ListView):
    model = Bar

class BarDetailView(generic.DetailView):
    model = Bar
