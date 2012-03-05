from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery, PhotoGalleryItem
from jaam.videos.models import Video, VideoGallery
from jaam.stories.models import Story
from jaam.blog.models import Blog, BlogPost
from easy_thumbnails.files import get_thumbnailer

#Search Imports
from django.conf.urls.defaults import *
from django.core.paginator import Paginator, InvalidPage
from haystack.query import SearchQuerySet
from tastypie.utils import trailing_slash
from django.http import Http404

import ast

class ProjectResource(ModelResource):
    covergallery = fields.ForeignKey('jaam.api.resources.PhotoGalleryResource', 'coverGallery', null=True)
    class Meta:
        queryset = Project.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'pk': ALL,
            'id': ALL,
            'slug': ALL,
            'covergallery': ('isnull'),
        }

class ProjectSearchResource(ModelResource):
    class Meta:
        queryset = Project.published_objects.all()
        resource_name = 'projects'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        # Do the query
        sqs = SearchQuerySet().models(Project).load_all().auto_query(request.GET.get('q', ''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)

class BlogPostSearchResource(ModelResource):
    class Meta:
        queryset = BlogPost.published_objects.all()
        resource_name = 'blog'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        # Do the query
        sqs = SearchQuerySet().models(BlogPost).load_all().auto_query(request.GET.get('q', ''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


class PhotoGalleryResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = PhotoGallery.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'project': ALL_WITH_RELATIONS,
        }

class PhotoResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Photo.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'slug': ALL,
            'project': ALL_WITH_RELATIONS,
            'title': ALL,
        }
    def dehydrate_image(self, bundle):
        if 'size' in bundle.request.GET:
            # TODO:
            # use id to filter instead of slug? implement id filtering above
            try:
                size = ast.literal_eval(bundle.request.GET['size'])
            except SyntaxError:
                return bundle.data['image']
            thumbnailer = self.obj_get(slug=bundle.data['slug']).image
            thumbnail_options = {'size': size}
            if 'crop' in bundle.request.GET and bundle.request.GET['crop'].lower() == 'true':
                thumbnail_options.update({'crop': True})
            return thumbnailer.get_thumbnail(thumbnail_options).url
        else:
            return bundle.data['image']
    def get_object_list(self, request):
        if hasattr(request, 'GET') and 'gallery__id' in request.GET:
            return Photo.published_objects.filter(photogallery=request.GET['gallery__id']).order_by('photogalleryitem__order')
        else:
            return super(PhotoResource, self).get_object_list(request)

class VideoGalleryResource(ModelResource):
    class Meta:
        queryset = VideoGallery.published_objects.all()
        allowed_methods = ['get']

class VideoResource(ModelResource):
    class Meta:
        queryset = Video.published_objects.all()
        allowed_methods = ['get']

class StoryResource(ModelResource):
    class Meta:
        queryset = Story.published_objects.all()
        allowed_methods = ['get']

class BlogResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Blog.published_objects.all()
        allowed_methods = ['get']

class BlogPostResource(ModelResource):
    class Meta:
        queryset = BlogPost.published_objects.all()
        allowed_methods = ['get']

class DocumentResource(ModelResource):
    # TODO:
    # this one could be interesting
    # check the TastyPie documentation on
    # non-ORM resources, which is what this would be.
    # 
    # It will need to build a QuerySet of documents
    # from DocumentCloud
    class Meta:
        pass
