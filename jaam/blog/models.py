from django.db import models
from django.contrib.auth.models import User
from jaam.journalism.models import BaseModel
from jaam.projects.models import Project
from ckeditor.fields import RichTextField

class Blog(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class BlogPost(BaseModel):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    body = RichTextField()
    author = models.OneToOneField(User)

    def __unicode__(self):
        return self.headline
