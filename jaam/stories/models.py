from django.db import models
from django.contrib.auth.models import User
from django.contrib.comments.moderation import CommentModerator, moderator
import datetime
from jaam.projects.models import Project
from jaam.journalism.models import BaseModel
from jaam.photos.models import Photo
from ckeditor.fields import RichTextField

# Create your models here.
class Story(BaseModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(User, limit_choices_to = { 'groups__name': "Journalists" })
    title = models.CharField(max_length=200)
    body = RichTextField()
    blurb = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(
        verbose_name='Date published:',
        default=datetime.datetime.now
        )
    enable_comments = models.BooleanField()
    cover_photo = models.ForeignKey(Photo, default= lambda: Photo.objects.get(title="Default"), on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"


    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.stories.views.details', (), {
            'project_slug': self.project.slug,
            'story_slug': self.slug,
        })
