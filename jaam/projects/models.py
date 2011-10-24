from django.db import models
from jaam.journalism.models import BaseModel

class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.location

class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    locations = models.ManyToManyField(ProjectLocation)

    def __unicode__(self):
        return self.title
