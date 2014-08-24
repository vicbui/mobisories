from django.conf.urls import patterns, url
from mobisories import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))