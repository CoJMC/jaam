from django.db import models
from jaam.journalism.models import BaseModel
from ckeditor.fields import RichTextField

class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.location

class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    locations = models.ManyToManyField(ProjectLocation)
    coverGallery = models.ForeignKey('photos.PhotoGallery', null=True, related_name='+')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.projects.views.details', (), {
            'project_slug': self.slug,
        })
