from django.db import models
from jaam.journalism.models import BaseModel, Journalist
from jaam.projects.models import Project
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import urllib2 as urllib
from cStringIO import StringIO
import datetime

class PhotoExifData(models.Model):
    camera_manufacturer = models.CharField(max_length=50, null=True)
    camera_model = models.CharField(max_length=50, null=True)
    date = models.DateTimeField('date photographed', null=True)
    shutter_speed = models.CharField(max_length=15, null=True)
    fnumber = models.CharField(max_length=15, null=True)
    focal_length = models.CharField(max_length=15, null=True)
    flash_used = models.NullBooleanField(null=True)
    height_dimension = models.CharField(max_length=15, null=True)
    width_dimension = models.CharField(max_length=15, null=True)
    gps_latitude = models.CharField(max_length=15, null=True)
    gps_longitude = models.CharField(max_length=15, null=True)
    altitude = models.CharField(max_length=15, null=True)
    
    def __unicode__(self):
        return ' '.join({self.camera_manufacturer, self.camera_model, self.date.__str__()})

class Photo(BaseModel):
    journalist = models.ForeignKey(Journalist)
    project = models.ForeignKey(Project)
    image = ThumbnailerImageField(('Image'),
                                height_field='',
                                width_field='',
                                upload_to='uploads/photos',
                                max_length=200)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=5000)
    exif_data = models.OneToOneField(PhotoExifData, blank=True, null=True)
    
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

@receiver(post_save, sender=Photo)
def pregenerate_thumbnails(sender, **kwargs):
    # generate thumbnails here, if desired.
    # still has to be offloaded to celery if we don't want to block rendering
    # we can probably get away with rendering them as needed and not bothering with the extra complexity involved
    pass

@receiver(pre_save, sender=Photo)
def create_exif(sender, instance, **kwargs):
    if instance.exif_data is None:
        exif = PhotoExifData()
        exif.save()
        instance.exif_data = exif

@receiver(post_save, sender=Photo)
def read_exif(sender, instance, **kwargs):
    img_file = urllib.urlopen(instance.image.url)
    im = StringIO(img_file.read())
    image = Image.open(im)

    data = dict((TAGS[k], v) for (k,v) in image._getexif().items() if (k in TAGS))
    exif = instance.exif_data
    exif.camera_manufacturer = data['Make'] if ('Make' in data) else None
    exif.camera_model = data['Model'] if ('Model' in data) else None
    exif.date = parse_datetime(data['DateTime']) if ('DateTime' in data) else None
    exif.shutter_speed = data['ExposureTime'] if ('ExposureTime' in data) else (data['ShutterSpeedValue'] if (['ShutterSpeedValue'] in data) else None)
    exif.fnumber = data['FNumber'] if ('FNumber' in data) else None
    exif.focal_length = data['FocalLength'] if ('FocalLength' in data) else None
    exif.flash_used = parse_flash(data['Flash']) if ('Flash' in data) else None
    exif.height_dimension = data['ExifImageHeight'] if ('ExifImageHeight' in data) else None
    exif.width_dimension = data['ExifImageWidth'] if ('ExifImageWidth' in data) else None
    
    gps_data = dict((GPSTAGS[k], v) for (k, v) in data['GPSInfo']) if ('GPSInfo' in data) else {}
    exif.gps_latitude = gps_data['GPSLatitude'] if ('GPSLatitude' in gps_data) else None
    exif.gps_longitude = gps_data['GPSLongitude'] if ('GPSLongitude' in gps_data) else None
    exif.altitude = gps_data['GPSAltitude'] if ('GPSAltitude' in gps_data) else None
    
    exif.save()

def parse_datetime(dt):
    #somehow detect other formats?
    dt_format = "%Y:%m:%d %H:%M:%S"
    return datetime.datetime.strptime(dt, dt_format)

def parse_flash(value):
    return False if (value == 0|16|24|32) else True