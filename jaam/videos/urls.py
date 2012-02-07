from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.videos.views',
    url(r'^$', 'index'),
    url(r'^galleries/(?P<gallery_slug>[^\\]+)/$', 'gallery_details'),
    url(r'^(?P<video_id>\d+)/$', 'details'),
)
