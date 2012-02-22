from django.conf.urls.defaults import patterns, include, url

# these urlmatch pattern should have a trailing slash IF AND ONLY IF there is an include('subapp.urls') reference for the routing
urlpatterns = patterns('',
    url(r'^(?P<project_slug>[^\/]+)/blog/', include('jaam.blog.urls')),
    url(r'^(?P<project_slug>[^\/]+)/photos/?', include('jaam.photos.urls')),
    url(r'^(?P<project_slug>[^\/]+)/photogalleries', 'jaam.photos.views.galleries'),
    url(r'^(?P<project_slug>[^\/]+)/videos/', include('jaam.videos.urls')),
    url(r'^(?P<project_slug>[^\/]+)/stories/', include('jaam.stories.urls')),
    url(r'^(?P<project_slug>[^\/]+)/documents/', include('jaam.document.urls')),
    url(r'^(?P<project_slug>[^\/]+)/act/', include('jaam.act.urls')),
    url(r'^(?P<project_slug>[^\/]+)/contributors', 'jaam.projects.views.contributors'),
    url(r'^(?P<project_slug>[^\/]+)', 'jaam.projects.views.details'),

)