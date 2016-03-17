from django.shortcuts import render

# Create your views here.

from django.views.generic import View, FormView,TemplateView,DeleteView

from django.http import HttpResponse

class VistaPrueba(View):

    def get(self, request, *args, **kwargs):
        return 'test'
