from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.journalism.views', 
    url(r'^(?P<username>\d+)/$', 'user_profile'),
    url(r'^(?P<username>\d+)/(?P<embedded>\d+)/$', 'user_profile'),                       
)