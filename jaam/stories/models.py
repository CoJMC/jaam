from django.db import models
from django.contrib.auth.models import User
from jaam.projects.models import Project
from jaam.journalism.models import Journalist, BaseModel
from ckeditor.fields import RichTextField

# Create your models here.
class Story(BaseModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(User)
    headline = models.CharField(max_length=200)
    body = RichTextField()
    blurb = models.CharField(max_length=1000)
    class Meta:
        verbose_name = "story"
        verbose_name_plural = "stories"

    def __unicode__(self):
        return self.headline

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.stories.views.details', (), {
            'project_slug': self.project.slug,
            'story_slug': self.slug,
        })
