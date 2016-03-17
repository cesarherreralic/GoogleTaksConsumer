# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.views.generic import View, FormView,TemplateView,DeleteView

from django.http import HttpResponse

from mysite.myhome import pull
from pull import *

from datetime import datetime

def home(request):

    myvar = 'this text is actually pulled from the server'
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    context = {
        "myvar": myvar,
        "testing": google_pull(),
        "client_id": "225698428296-vtgu502l3h3tvbe58ccmjkmjlvvsjtnk.apps.googleusercontent.com",
        "tasks":[
                {"id": 1, "name":"New Job", "description": "I want this job", "startdate": now, "enddate": now, "status": "completed"  }
            ]

    }

    return render(request, 'home.html', context)

def event(request):

    myvar = 'this text is actually pulled from the server'
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    context = {
        "myvar": myvar,
        "testing": google_pull(),
        "client_id": "225698428296-4vug4vo8o2na8gm2bfk32deaqrqhqb5j.apps.googleusercontent.com",
        "tasks":[
                {"id": 1, "name":"New Job", "description": "I want this job", "startdate": now, "enddate": now, "status": "completed"  }
            ]

    }

    return render(request, 'event.html', context)

#class Home2(View):
#
#    def get(self, request, *args, **kwargs):
#        return 'test'

