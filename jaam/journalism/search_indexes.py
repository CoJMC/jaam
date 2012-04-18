import haystack
from haystack import indexes
from django.contrib import admin
from blog.models import Blog, BlogPost
# Not sure about UserProfile
from journalism.models import UserProfile
from photos.models import Photo
from projects.models import Project
from stories.models import Story
from videos.models import Video

class BlogPostIndex(indexes.SearchIndex, indexes.Indexable):
	# journalist = indexes.CharField(model_attr='journalist')
	# title = indexes.CharField(model_attr='title')
	text = indexes.CharField(document=True, use_template=True)


	def get_model(self):
		return BlogPost


	def index_queryset(self):
        # Used when the entire index for model is updated.
        #filter by published
		return self.get_model().objects.filter(published=True)


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
	# title_value = indexes.CharField(model_attr='title')
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Project

	def index_queryset(self):
        # Used when the entire index for model is updated.
        #filter by published
		return self.get_model().objects.filter(published=True)

class StoryIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Story

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Video

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)


class PhotoIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	journalist = indexes.CharField(model_attr='journalist');

	def get_model(self):
		return Photo

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)




# No registering is needed in Haystack 2.x
#site.register(BlogPost, BlogPostIndex)
#site.register(Project, ProjectIndex)
#site.register(Story, StoryIndex)
#site.register(Video, VideoIndex)
#site.register(Photo, PhotoIndex)
