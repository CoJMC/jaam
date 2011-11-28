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
    url(r'^accounts/profile', 'jaam.journalism.views.login_dump'),
    # enable ckeditor path
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^act/', include('jaam.act.urls')),
    url(r'^journalism', include('jaam.journalism.urls')),
    url(r'^projects/', include('jaam.projects.urls')),
    url(r'^users/(?P<username>[^\\]+)/', 'jaam.journalism.views.user_profile'),
    url(r'^activate_layout/(?P<layout_name>[^\\]+)/', 'jaam.journalism.views.activate_layout'),
    url(r'^$', 'jaam.projects.views.index'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="auth_logout"),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }))
