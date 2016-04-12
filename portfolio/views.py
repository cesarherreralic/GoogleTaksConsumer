# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import View, FormView,TemplateView,DeleteView
from django.contrib.auth import authenticate, login, logout, hashers
from django.contrib import messages
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from datetime import datetime

import json


class Portfolio(View):
    """ Class to register users """

    def dispatch(self, request, *args, **kwargs):
        return super(Portfolio, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        return render(request,'portfolio.html')