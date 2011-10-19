from django.db import models
from jaam.projects.models import Project
from jaam.journalism.models import Journalist, BaseModel

# Create your models here.
class Story(BaseModel):
    project = models.ForeignKey(Project)
    author = models.ForeignKey(Journalist)
    headline = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    blurb = models.CharField(max_length=1000)