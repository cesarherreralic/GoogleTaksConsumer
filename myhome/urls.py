from django.conf.urls.defaults import patterns, include, url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^events/', views.event, name='event'),
]
