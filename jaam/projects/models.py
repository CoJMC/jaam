from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.sites.models import Site
from jaam.journalism.models import BaseModel, User
from ckeditor.fields import RichTextField
import re


class ProjectLocation(models.Model):
    location = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.location

class Project(BaseModel):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=250)
    primaryColor = models.CharField(max_length=7,default="FF0000")
    accentColor = models.CharField(max_length=7, default="FFFFFF")
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    locations = models.ManyToManyField(ProjectLocation)
    coverGallery = models.ForeignKey('photos.PhotoGallery', null=True, blank=True, related_name='+')
    archived = models.BooleanField(default = False)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('jaam.projects.views.details', (), {
            'project_slug': self.slug,
        })
    def rss_urls(self):
        from jaam.feeds import LatestPhotosFeed, LatestStoriesFeed, LatestBlogsFeed
        domain = Site.objects.get_current().domain
        photos = "<a href='%s'>Photos</a><br>" % LatestPhotosFeed().link(self)
        stories = "<a href='%s'>Stories</a><br>" % LatestStoriesFeed().link(self)
        blog_posts = "<a href='%s'>Blog Posts</a>" % LatestBlogsFeed().link(self)
        return photos + stories + blog_posts
    rss_urls.allow_tags = True

    @property
    def journalists(self):
        journalist_ids = list(self.photo_set.all().values_list('journalist', flat=True))
        journalist_ids.extend(self.video_set.all().values_list('journalist', flat=True))
        journalist_ids.extend(self.story_set.all().values_list('author', flat=True))
        journalist_ids.extend(self.blog_set.all().values_list('blogpost__author', flat=True))
        return User.objects.filter(
            pk__in=journalist_ids
        )

@receiver(pre_save, sender=Project)
def format_colors(instance, **kwargs):
    p_length = len(instance.primaryColor)
    a_length = len(instance.accentColor)
    if (p_length is 3 or p_length is 6) and is_hex(instance.primaryColor):
        instance.primaryColor = "#" + instance.primaryColor.upper()
    if (a_length is 3 or a_length is 6) and is_hex(instance.accentColor):
        instance.accentColor = "#" + instance.accentColor.upper()

def is_hex(value):
    search = re.compile(r'[^0-9a-fA-F]').search
    return not bool(search(value))
