from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.photos.views',
    url(r'^galleries/(?P<gallery_slug>[^\\]+)/(?P<start_number>[^\\]+)/$', 'gallery_details', name="start_photo_gallery"),
    url(r'^galleries/(?P<gallery_slug>[^\\]+)/$', 'gallery_details'),
    url(r'^(?P<photo_id>\d+)/$', 'details'),
    url(r'^exif/(?P<photo_id>\d+)/$', 'exif'),
    url(r'^$', 'galleries'),
)
