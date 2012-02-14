from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from tastypie.api import Api
from jaam import settings
from jaam.api.resources import ProjectResource, PhotoGalleryResource, PhotoResource, VideoGalleryResource
from jaam.api.resources import VideoResource, StoryResource, BlogResource, BlogPostResource, DocumentResource

admin.autodiscover()

# TASTYPIE INITIALIZATION
v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())
v1_api.register(PhotoGalleryResource())
v1_api.register(PhotoResource())
v1_api.register(VideoGalleryResource())
v1_api.register(VideoResource())
v1_api.register(StoryResource())
v1_api.register(BlogResource())
v1_api.register(BlogPostResource())
v1_api.register(DocumentResource())

urlpatterns = patterns('',
    # ADMIN
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    #comment
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # CKEDITOR
    (r'^ckeditor/', include('ckeditor.urls')), # TODO: Is this necessary

    # JAAM
    url(r'^act/', include('jaam.act.urls')),
    url(r'^journalism/', include('jaam.journalism.urls')),
    url(r'^projects/', include('jaam.projects.urls')),
    url(r'^$', 'jaam.projects.views.index'), # TODO ????
    #(r'^$', direct_to_template, {'template': 'projects/index.html'}),

    # USER / AUTH
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="auth_logout"),
    url(r'', include('social_auth.urls')),
    url(r'^accounts/profile', 'jaam.journalism.views.profile_set'), # TODO: This goes in the journalism project
    url(r'^confirm', 'jaam.journalism.views.profile_set'), # TODO: This too
    url(r'^users/(?P<username>[^\\]+)/', 'jaam.journalism.views.user_profile'), # TODO: Probably goes in the journalism app too
    url(r'^act_information', 'jaam.act.views.information'),
    url(r'^about_us', 'jaam.journalism.views.about'),
    # REST API
    (r'^api/', include(v1_api.urls)),

    # REST UI CONSUMER
    (r'roy/', direct_to_template, {'template': 'roy/index.html'})
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }))
