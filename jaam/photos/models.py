from django.db import models
from jaam.journalism.models import BaseModel, Journalist
from jaam.projects.models import Project
    
class PhotoExifData(models.Model):
    camera_manufacturer = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=100)
    date = models.DateTimeField('date photographed')
    shutter_speed = models.CharField(max_length=50)
    aperture = models.CharField(max_length=50)
    focal_length = models.CharField(max_length=50)
    flash_used = models.BooleanField()
    height_dimension = models.CharField(max_length=50)
    width_dimension = models.CharField(max_length=50)
    gps_latitude = models.CharField(max_length=50)
    gps_longitude = models.CharField(max_length=50)
    altitude = models.CharField(max_length=50)
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
    class Meta:
        verbose_name = "photo gallery"
        verbose_name_plural = "photo galleries"

    def __unicode__(self):
        return self.title
