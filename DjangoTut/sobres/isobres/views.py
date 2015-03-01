from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Sobres aPP',
        'pagetitle': 'Welcome to the Sobres aPPlication',
        'contentbody': 'Managing non legal funding since 2013'
        })
    output = template.render(variables)
    return HttpResponse(output)

