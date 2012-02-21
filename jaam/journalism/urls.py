from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.journalism.views', 
                       url(r'^(?P<user_slug>\d+)/$', 'user_profile'),   
)
