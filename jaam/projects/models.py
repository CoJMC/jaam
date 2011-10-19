from django.db import models
from jaam.jaam.models import BaseModel

class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    
class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)
    project = models.ForeignKey(Project)
    pass