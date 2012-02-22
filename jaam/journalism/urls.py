from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.journalism.views', 
                       url(r'^(?P<username>\d+)/$', 'user_profile'),   
)
