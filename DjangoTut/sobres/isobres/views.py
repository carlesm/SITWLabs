from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User


# Create your views here.
def mainpage(request):
   return render_to_response(
        'mainpage.html',
        {
                'titlehead': 'Sobres aPP',
                'pagetitle': 'Welcome to the Sobres aPPlication',
                'contentbody': 'Managing non legal funding since 2013',
                'user': request.user
        })




def userpage(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('User not found.')

    sobres = user.sobre_set.all()
    template = get_template('userpage.html')
    variables = Context({
        'username': username,
        'sobres': sobres
        })
    output = template.render(variables)
    return HttpResponse(output)

