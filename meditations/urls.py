from django.conf.urls import patterns, url

from meditations import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
