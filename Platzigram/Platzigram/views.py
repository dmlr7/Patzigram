"""Platzigram views"""
#djanjo
from django.http import HttpResponse
#utilities
from datetime import datetime
import json
import pdb

from django.urls import resolvers

def hello_world(request):
    """ Return a greeting """
    return HttpResponse(f'oh hi, currrent server time is:\
        {datetime.now().strftime("%dth %b, %Y - %H:%M hrs")},')

def sorted_integers(request):
    """ Return order numbers y array gevien"""
    temporal = [int(i) for i in request.GET['numbers'].split(",")]
    temporal.sort()
    data = {'status': 'ok',
            'numbers': temporal,
            'message': 'Integers sorted successfully.',
            }
    return HttpResponse(json.dumps(data,indent=4),
        content_type='application/json')

def say_hi(request, name, age):
    """return a greeting"""
    if age  < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, welcome'
    return HttpResponse(message)