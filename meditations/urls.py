from django.conf.urls import patterns, include, url

from meditations import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^id/(?P<meditation_id>\d+)/$', views.id, name='id'),
)
