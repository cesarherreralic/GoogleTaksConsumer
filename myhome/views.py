# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import View, FormView,TemplateView,DeleteView
from django.contrib.auth import authenticate, login, logout, hashers
from django.contrib import messages
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from myhome.forms import *

from myhome import pull
from pull import *

from datetime import datetime

import json

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


def sea3d(request):
    """ View to render template for sea3d object loader with three.js """
    return render(request, 'sea3dloader/sea3d.html')


def conference(request):

    me = None
    try:
        if(request.user.is_authenticated()):
            me = request.user
    except Exception as e:
        print e

    if me == None:
        me = 'Anonymous User'
        return redirect(reverse_lazy('login'))
    else:
        me = me.username

    context = {
        "user_id": 'name pulled from db',
        "me": me
    }

    return render(request, 'conference.html', context)



class Login(FormView):

    form_class = AutenticationUserForm
    template_name = 'register/login.html'
    success_url = reverse_lazy('conference')


    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            return redirect(reverse_lazy('conference'))


        return super(Login, self).dispatch(request, *args, **kwargs)




    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
            else:
                return redirect(reverse_lazy('login'))

        return super(Login, self).form_valid(form)


class RegisterUser(View):
    """ Class to register users """

    def dispatch(self, request, *args, **kwargs):
        return super(RegisterUser, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        form = UserForm()
        context = {'form': form }
        return render(request,'register/register.html', context)

    def post(self, request, *args, **kwargs):

        data = {}
        form = UserForm(request.POST)

        # Let's validate whether user exists or not
        user_exists = True
        try:
            usuario_existente = User.objects.get(email=form.data['email'], username=form.data['username'])
        except User.DoesNotExist:
            user_exists = False


        if user_exists:
            message_context = { 'message': 'The user already exists.',
                        'message_header': 'Error',
                        'message_title': 'User already exists' }
            return render(request,'register/register.html', message_context)

        if form.is_valid():

            f=form.save(commit=False)
            f.is_active = True
            #f.password = hashers.make_password(f.password)
            f.set_password(form.data['password'])
            f.save()

            data = {}
            data['Result'] = 'success'
            return HttpResponse(json.dumps(data), content_type = "application/json")

        data = {}
        data['Result'] = 'error'
        data['formularios']='errores'
        data['form']=json.dumps(form.errors)

        return HttpResponse(json.dumps(data), content_type = "application/json")


class Logout(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            mensaje = u'Session closed successfully'
            messages.info(self.request, mensaje)
        return redirect(reverse_lazy('login'))

#class Home2(View):
#
#    def get(self, request, *args, **kwargs):
#        return 'test'

