from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jaam.views.home', name='home'),
    # url(r'^jaam/', include('jaam.foo.urls')),

    # enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # enable the social auth login urls
    url(r'', include('social_auth.urls')),
)