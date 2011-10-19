from django.db import models
<<<<<<< HEAD
=======
from jaam.journalism.models import BaseModel
>>>>>>> d47faba09693d7a2d41de4362561f291d7a221bb

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    
class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)
    project = models.ForeignKey(Project)
    pass
