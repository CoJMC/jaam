from django.db import models
from django.contrib.auth.models import User
from jaam.journalism.models import BaseModel
from jaam.projects.models import Project
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import urllib2 as urllib
from cStringIO import StringIO
import datetime
from django.contrib.comments.signals import comment_was_posted
from django.utils.encoding import smart_str
import akismet
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.comments.moderation import CommentModerator, moderator

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
        return ' '.join({self.photo.project.title, self.photo.title})

class Photo(BaseModel):
    journalist = models.ForeignKey(User, limit_choices_to = { 'groups__name': "Journalists" })
    project = models.ForeignKey(Project)
    image = ThumbnailerImageField(('Image'),
                                height_field='',
                                width_field='',
                                upload_to='uploads/photos',
                                max_length=200)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=5000)
    exif_data = models.OneToOneField(PhotoExifData, blank=True, null=True, editable=False)
    enable_comments = models.BooleanField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.photos.views.details', (), {
            'project_slug': self.project.slug,
            'photo_id': self.id,
        })

    @property
    def comments_expired(self):
        delta = datetime.datetime.now() - self.pub_date
        return delta.days < 90
    
    @property
    def photos(self):
        return Photo.objects.filter(
            pk__in=self.project.photo_set.all().values_list('journalist', flat=True).query
        )

#Akismet spam connections
def moderate_comment(sender, comment, request, **kwargs):
    ak = akismet.Akismet(
        key = settings.AKISMET_API_KEY,
            blog_url = 'http://%s/' % Site.objects.get_current().domain
)
    data = {
        'user_ip': request.META.get('REMOTE_ADDR', ''),
        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
        'referrer': request.META.get('HTTP_REFERRER', ''),
        'comment_type': 'comment',
        'comment_author': smart_str(comment.user_name),
    }
    if ak.comment_check(smart_str(comment.comment), data=data, build_data=True):
        comment.is_public = False
        comment.save()
        print "SPAM"
    else:
        print "JAAM"

comment_was_posted.connect(moderate_comment)


class PhotoModerator(CommentModerator):
    email_notification = False
    enable_field = 'enable_comments'

moderator.register(Photo, PhotoModerator)

class PhotoGallery(BaseModel):
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=5000)
    project = models.ForeignKey(Project)
    photos = models.ManyToManyField(Photo, through="PhotoGalleryItem")

    class Meta:
        verbose_name = "photo gallery"
        verbose_name_plural = "photo galleries"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.photos.views.gallery_details', (), {
            'project_slug': self.project.slug,
            'gallery_slug': self.slug,
        })

    @property
    def cover_photo(self):
        return self.photogalleryitem_set.order_by('order')[0].photo
# This is for ordering photos inside of photo galleries which can't be done with
# a regular m2m relationship
class PhotoGalleryItem(models.Model):
    photo = models.ForeignKey(Photo)
    order = models.IntegerField(null=True)
    gallery = models.ForeignKey(PhotoGallery)

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

    try:
        photo_exif = image._getexif()
        data = dict((TAGS[k], v) for (k,v) in photo_exif.items() if (k in TAGS))
    except AttributeError:
        return

    exif = instance.exif_data
    exif.camera_manufacturer = data['Make'] if ('Make' in data) else None
    exif.camera_model = data['Model'] if ('Model' in data) else None
    exif.date = parse_datetime(data['DateTime']) if ('DateTime' in data) else None
    exif.shutter_speed = parse_shutterspeed(data['ExposureTime']) if ('ExposureTime' in data) else (data['ShutterSpeedValue'] if ('ShutterSpeedValue' in data) else None)
    exif.fnumber = parse_fnumber(data['FNumber']) if ('FNumber' in data) else None
    exif.focal_length = parse_focallength(data['FocalLength']) if ('FocalLength' in data) else None
    exif.flash_used = parse_flash(data['Flash']) if ('Flash' in data) else None
    exif.height_dimension = data['ExifImageHeight'] if ('ExifImageHeight' in data) else None
    exif.width_dimension = data['ExifImageWidth'] if ('ExifImageWidth' in data) else None

    gps_data = dict((GPSTAGS[k], v) for (k, v) in data['GPSInfo'].items() if (k in GPSTAGS)) if ('GPSInfo' in data) else {}

    exif.gps_latitude = gps_data['GPSLatitude'] if ('GPSLatitude' in gps_data) else None
    exif.gps_longitude = gps_data['GPSLongitude'] if ('GPSLongitude' in gps_data) else None
    exif.altitude = gps_data['GPSAltitude'] if ('GPSAltitude' in gps_data) else None

    exif.save()

def parse_datetime(dt):
    # is this format standard in all exif data?
    dt_format = "%Y:%m:%d %H:%M:%S"
    return datetime.datetime.strptime(dt, dt_format)

def parse_shutterspeed(value):
    return str(value[0]) + "/" + str(value[1])

def parse_fnumber(value):
    return float(value[0]) / float(value[1])

def parse_focallength(value):
    return str(float(value[0]) / float(value[1])) + " mm"

def parse_flash(value):
    return False if (value == 0|16|24|32) else True
