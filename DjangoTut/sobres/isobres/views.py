from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import simplejson

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


def sobresjson(request):
    user = request.user
    if not user:
        raise Http404('User not found.')
    sobres = user.sobre_set.all()
    sobresjson = []
    for s in sobres:
        sobre = dict()
        sobre["date"]=s.date.ctime()
        sobre["amount"]=s.amount
        sobre["concept"]=s.concept
        sobre["donor"]=s.donor.name
        sobre["user"]=s.user.username
        sobresjson.append(sobre)


    return HttpResponse(simplejson.dumps(sobresjson),mimetype='application/json')

