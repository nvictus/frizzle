from django.conf.urls import patterns, url

from frizzle.polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)