from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from jaam.blog.models import BlogPost
from jaam.stories.models import Story
from jaam.photos.models import Photo
from jaam.projects.models import Project


class LatestBlogsFeed(Feed):
    def title(self, obj):
        return obj.title + ' Blog Posts'

    def link(self, obj):
        domain = Site.objects.get_current().domain
        project_slug = obj.slug
        return "/feeds/%s/blog_posts.rss" % (project_slug)

    def description(self, obj):
        return obj.title + ' Blog Posts'

    def get_object(self, request, *args, **kwargs):
        project = Project.objects.get(slug=kwargs['project_slug'])
        return project

    def items(self, obj):
        return BlogPost.objects.filter(blog__project__id=obj.id).all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.get_absolute_url()

class LatestStoriesFeed(Feed):
    def title(self, obj):
        return obj.title + ' Stories'

    def link(self, obj):
        domain = Site.objects.get_current().domain
        project_slug = obj.slug
        return "/feeds/%s/stories.rss" % (project_slug)

    def description(self, obj):
        return obj.title + ' Stories'

    def get_object(self, request, *args, **kwargs):
        project = Project.objects.get(slug=kwargs['project_slug'])
        return project

    def items(self, obj):
        return Story.objects.filter(project__id=obj.id).all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.get_absolute_url()

class LatestPhotosFeed(Feed):
    def title(self, obj):
        return obj.title + ' Photos'

    def link(self, obj):
        domain = Site.objects.get_current().domain
        project_slug = obj.slug
        return "/feeds/%s/photos.rss" % (project_slug)
        
    def description(self, obj):
        return obj.title + ' Photos'

    def get_object(self, request, *args, **kwargs):
        project = Project.objects.get(slug=kwargs['project_slug'])
        return project

    def items(self, obj):
        return Photo.objects.filter(project__id=obj.id).all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return '<img src="'+item.image.url+'">'

    def item_link(self, item):
        return item.get_absolute_url()
