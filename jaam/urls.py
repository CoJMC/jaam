from django.conf.urls.defaults import patterns, include, url
from jaam import settings

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
    # enable ckeditor path
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^act/', include('jaam.act.urls')),
    url(r'^blog/', include('jaam.blog.urls')),
    url(r'^document/', include('jaam.document.urls')),
    url(r'^journalism', include('jaam.journalism.urls')),
    url(r'^photos/', include('jaam.photos.urls')),
    url(r'^projects/', include('jaam.projects.urls')),
    url(r'^stories/', include('jaam.stories.urls')),
    url(r'^videos/', include('jaam.videos.urls')),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }))
