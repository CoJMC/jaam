from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery
from jaam.videos.models import Video, VideoGallery
from jaam.stories.models import Story
from jaam.blog.models import Blog, BlogPost
from easy_thumbnails.files import get_thumbnailer
import ast

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        allowed_methods = ['get']

class PhotoGalleryResource(ModelResource):
    class Meta:
        queryset = PhotoGallery.objects.all()
        allowed_methods = ['get']

class PhotoResource(ModelResource):
    class Meta:
        queryset = Photo.objects.all()
        allowed_methods = ['get']
        filtering = {
            'slug': ALL,
            'project': ALL_WITH_RELATIONS,
            'journalist': ALL,
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
            return thumbnailer.get_thumbnail(thumbnail_options).url
        else:
            return bundle.data['image']

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
