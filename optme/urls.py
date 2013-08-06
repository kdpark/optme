from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'optme.views.home', name='home'),
    url(r'^calculator/', 'reverse.views.main'),

    url(r'^admin/', include(admin.site.urls)),
)
