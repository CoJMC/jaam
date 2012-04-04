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

class BaseModelResource(ModelResource):
    pass

class SearchResource(BaseModelResource):
    class Meta:
        resource_name = "search";
        queryset = Project.published_objects.all()

    def get_object_list(self, request):
        return Project.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(SearchResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters


class ProjectResource(BaseModelResource):
    covergallery = fields.ForeignKey('jaam.api.resources.PhotoGalleryResource', 'coverGallery', null=True)
    class Meta:
        queryset = Project.published_objects
        allowed_methods = ['get']
        filtering = {
            'pk': ALL,
            'id': ALL,
            'slug': ALL,
            'archived': ALL,
            'covergallery': ('isnull'),
        }    

    def get_object_list(self, request):
        return Project.published_objects

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(ProjectResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class PhotoGalleryResource(BaseModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = PhotoGallery.published_objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'project': ALL_WITH_RELATIONS,
        }

    def get_object_list(self, request):
        return PhotoGallery.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PhotoGalleryResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class PhotoResource(BaseModelResource):
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
            return Photo.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PhotoResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class VideoGalleryResource(ModelResource):
    class Meta:
        queryset = VideoGallery.published_objects.all()
        allowed_methods = ['get']

    def get_object_list(self, request):
        return VideoGallery.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(VideoGalleryResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class VideoResource(BaseModelResource):
    class Meta:
        queryset = Video.published_objects.all()
        allowed_methods = ['get']

    def get_object_list(self, request):
        return Video.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(VideoResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class StoryResource(BaseModelResource):
    class Meta:
        queryset = Story.published_objects.all()
        allowed_methods = ['get']

    def get_object_list(self, request):
        return Story.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(StoryResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class BlogResource(BaseModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Blog.published_objects.all()
        allowed_methods = ['get']

    def get_object_list(self, request):
        return Blog.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(BlogResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class BlogPostResource(BaseModelResource):
    class Meta:
        queryset = BlogPost.published_objects.all()
        allowed_methods = ['get']

    def get_object_list(self, request):
        return BlogPost.published_objects.all()

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(BlogPostResource, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

class DocumentResource(BaseModelResource):
    # TODO:
    # this one could be interesting
    # check the TastyPie documentation on
    # non-ORM resources, which is what this would be.
    # 
    # It will need to build a QuerySet of documents
    # from DocumentCloud
    class Meta:
        pass



# There's a good chance none of this is needed, but I don't really want to delete it now to have to find it all later.
'''
class ProjectSearchResource(BaseModelResource):
    class Meta:
        queryset = Project.published_objects.all()
        resource_name = 'projectsearch'

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


class BlogPostSearchResource(BaseModelResource):
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

class VideoSearchResource(BaseModelResource):
    class Meta:
        queryset = Video.published_objects.all()
        resource_name = 'videos'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        # Do the query
        sqs = SearchQuerySet().models(Video).load_all().auto_query(request.GET.get('q', ''))
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
'''
