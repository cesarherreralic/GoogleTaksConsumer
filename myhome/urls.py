#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^events/', views.event, name='events'),
    url(r'^sea3d/', views.sea3d, name='sea3d'),
    url(r'^conference/', views.conference, name='conference'),
    url(r'^login/', views.Login.as_view(), name='login'),
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^logout/', views.Logout.as_view(), name='logout'),
    #url(r'^$', views.Login.as_view(), name='login'),
    url(r'^register/', views.RegisterUser.as_view(), name='register'),
    #url(r'^login/', views.Login.as_view(), name='login'),
    #url(r'^logout/', views.Logout.as_view(), name='login'),
    #url(r'^register/', views.RegisterUser.as_view(), name='register'),
]
