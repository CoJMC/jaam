from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('jaam.blog.views',
    url(r'^(?P<blog_title_slug>[^\\]+)/posts/(?P<blog_post_slug>[^\\]+)/$', 'post_details'),
    url(r'^(?P<blog_title_slug>[^\\]+)/$', 'blog_details'),
)
