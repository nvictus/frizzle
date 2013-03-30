from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import frizzle.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frizzle.views.home', name='home'),
    # url(r'^frizzle/', include('frizzle.foo.urls')),

    url(r'^$', frizzle.views.index, name='index'),
    url(r'^polls/', include('frizzle.polls.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
