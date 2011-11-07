from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.photos.views',
    url(r'^galleries/(?P<gallery_slug>[^\\]+)/$', 'gallery_details'),
    url(r'^(?P<photo_id>\d+)/$', 'details'),
)
