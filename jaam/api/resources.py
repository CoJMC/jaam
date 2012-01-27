from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery, PhotoGalleryItem
from jaam.videos.models import Video, VideoGallery
from jaam.stories.models import Story
from jaam.blog.models import Blog, BlogPost
from easy_thumbnails.files import get_thumbnailer
import ast

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        allowed_methods = ['get']
        filtering = {
            'pk': ALL,
            'id': ALL,
            'slug': ALL,
        }

class PhotoGalleryResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = PhotoGallery.objects.all()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            'project': ALL_WITH_RELATIONS,
        }

class PhotoResource(ModelResource):
    project = fields.ForeignKey(ProjectResource, 'project')
    class Meta:
        queryset = Photo.objects.all()
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
            # add a crop option {'crop': True}
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
    def build_filters(self, filters=None):
        # TODO Comment this
        if filters is None:
            filters = {}

        orm_filters = super(PhotoResource, self).build_filters(filters)

        if "gallery__id" in filters:
            pgi_items = PhotoGalleryItem.objects.filter(gallery__pk=filters['gallery__id'])
            print pgi_items
            print filters['gallery__id']
            orm_filters["pk__in"] = [i.photo.pk for i in pgi_items]

        return orm_filters

# class PhotoGalleryItemResource(ModelResource):
#     gallery = fields.ForeignKey(PhotoGalleryResource, 'gallery')
#     class Meta:
#         queryset = PhotoGalleryItem.objects.all()
#         allow_methods = ['get']
#         filtering = {
#             'gallery': ALL_WITH_RELATIONS,
#         }


class VideoGalleryResource(ModelResource):
    class Meta:
        quersyset = VideoGallery.objects.all()

class VideoGalleryResource(ModelResource):
    class Meta:
        queryset = VideoGallery.objects.all()
        allowed_methods = ['get']

class VideoResource(ModelResource):
    class Meta:
        queryset = Video.objects.all()
        allowed_methods = ['get']

class StoryResource(ModelResource):
    class Meta:
        queryset = Story.objects.all()
        allowed_methods = ['get']

class BlogResource(ModelResource):
    class Meta:
        queryset = Blog.objects.all()
        allowed_methods = ['get']

class BlogPostResource(ModelResource):
    class Meta:
        queryset = BlogPost.objects.all()
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
