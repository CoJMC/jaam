from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.stories.views',
    url(r'^(?P<story_slug>[^\\]+)/$', 'details'),
)
