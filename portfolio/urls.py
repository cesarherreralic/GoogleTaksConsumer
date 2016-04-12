#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^', views.Portfolio.as_view(), name='portfolio'),
]
