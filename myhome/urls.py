#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home),
    url(r'^events/', views.event),
    url(r'^conference/', views.conference),
    #url(r'^login/', views.Login.as_view(), name='login'),
    #url(r'^logout/', views.Logout.as_view(), name='login'),
    #url(r'^register/', views.RegisterUser.as_view(), name='register'),
]
