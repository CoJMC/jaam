from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.document.views',
    url(r'^(?P<document_slug>[^\\]+)/$', 'details'),
)
