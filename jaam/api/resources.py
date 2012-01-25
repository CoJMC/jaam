from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from jaam.projects.models import Project
from jaam.photos.models import Photo, PhotoGallery, PhotoGalleryItem
from jaam.videos.models import Video, VideoGallery
from jaam.stories.models import Story
from jaam.blog.models import Blog, BlogPost

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

class PhotoGalleryItemResource(ModelResource):
    class Meta:
        queryset = PhotoGalleryItem.objects.all()
        allow_methods = ['get']
        filtering = {
            'photo' : ALL_WITH_RELATIONS,
            'gallery': ALL_WITH_RELATIONS,
        }

class VideoGalleryResource(ModelResource):
    class Meta:
        quersyset = VideoGallery.objects.all()
        allowed_methods = ['get']

class VideoResource(ModelResource):
    class Meta:
        quersyset = Video.objects.all()
        allowed_methods = ['get']

class StoryResource(ModelResource):
    class Meta:
        quersyset = Story.objects.all()
        allowed_methods = ['get']

class BlogResource(ModelResource):
    class Meta:
        quersyset = Blog.objects.all()
        allowed_methods = ['get']

class BlogPostResource(ModelResource):
    class Meta:
        quersyset = BlogPost.objects.all()
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