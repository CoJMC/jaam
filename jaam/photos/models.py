from django.db import models
from jaam.journalism.models import BaseModel, Journalist
from jaam.projects.models import Project
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_save
from django.dispatch import receiver
    
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
    image = ThumbnailerImageField(('Image'),
                                height_field='',
                                width_field='',
                                upload_to='uploads/photos')   
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    exif_data = models.ForeignKey(PhotoExifData)
    
    def __unicode__(self):
        return self.title

class PhotoGallery(BaseModel):
    title = models.CharField(max_length=100)
    introduction = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project)
    class Meta:
        verbose_name = "photo gallery"
        verbose_name_plural = "photo galleries"

    def __unicode__(self):
        return self.title

@receiver(post_save, sender=Photo)
def pregenerate_thumbnails(sender, **kwargs):
    # generate thumbnails here, if desired.
    # still has to be offloaded to celery if we don't want to block rendering
    # we can probably get away with rendering them as needed and not bothering with the extra complexity involved
    pass
