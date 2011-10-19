from django.db import models
from jaam.jaam.models import BaseModel, Journalist
from jaam.projects.models import Project
    
class PhotoExifData(models.Model):
    pass

class Photo(BaseModel):
    journalist = models.ForeignKey(Journalist)
    project = models.ForeignKey(Project)
    image = models.ImageField(('Image'),
                                height_field='',
                                width_field='',
                                upload_to='uploads/photos',
                                max_length=200)   
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=5000)
    exif_data = models.ForeignKey(PhotoExifData)
    
    def __unicode__(self):
        return self.title

class PhotoGallery(BaseModel):
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=5000)
    project = models.ForeignKey(Project)
    pass