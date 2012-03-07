import haystack
from haystack import indexes, site
from django.contrib import admin
from blog.models import Blog, BlogPost
# Not sure about UserProfile
from journalism.models import UserProfile
from photos.models import Photo
from projects.models import Project
from stories.models import Story
from videos.models import Video

haystack.autodiscover()


class BlogPostIndex(indexes.SearchIndex):
	# author = indexes.CharField(model_attr='author')
	# title = indexes.CharField(model_attr='title')
	text = indexes.CharField(document=True, use_template=True)


	def get_model(self):
		return BlogPost


	def index_queryset(self):
        # Used when the entire index for model is updated.
        #filter by published
		return self.get_model().objects.filter(published=True)

	# TODO: use reg exp to remove html


class ProjectIndex(indexes.SearchIndex):
	# title_value = indexes.CharField(model_attr='title')
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Project

	def index_queryset(self):
        # Used when the entire index for model is updated.
        #filter by published
		return self.get_model().objects.filter(published=True)

	#  TODO: use reg exp to remove html

class StoryIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Story

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)


class VideoIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Video

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)


class PhotoIndex(indexes.SearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	author = indexes.CharField(model_attr='journalist');

	def get_model(self):
		return Photo

	def index_queryset(self):
		return self.get_model().objects.filter(published=True)





site.register(BlogPost, BlogPostIndex)
site.register(Project, ProjectIndex)
site.register(Story, StoryIndex)
site.register(Video, VideoIndex)
site.register(Photo, PhotoIndex)
