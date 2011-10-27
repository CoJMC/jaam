from django.db import models
from jaam.journalism.models import BaseModel, Journalist
from jaam.projects.models import Project

class Video(BaseModel):
    journalist = models.ForeignKey(Journalist)
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    videoUrl = models.CharField(max_length=20,)
    
    def __unicode__(self):
        return self.title

class VideoGallery(BaseModel):
    title = models.CharField(max_length=100)
    introduction = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project)
    class Meta:
        verbose_name = "video gallery"
        verbose_name_plural = "video galleries"

    def __unicode__(self):
        return self.title
